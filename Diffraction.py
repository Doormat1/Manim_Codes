from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
import numpy as np

class Diffraction(MovingCameraScene, VoiceoverScene):
    def create_grating(self, start_point, end_point, num_slits, slit_width=0.1):
        """Creates a vertical dashed-line style grating (stacked vertical segments)
        Args:
            start_point: Starting point of the grating (x, y, z)
            end_point: End point of the grating (x, y, z)
            num_slits: Number of slits (gaps) in the grating (number of gaps down the column)
            slit_width: unused for vertical segments but kept for API compatibility
        Returns:
            VGroup containing the grating segments and stores gap centers in self.gap_centers
        """
        grating = VGroup()
        total_height = end_point[1] - start_point[1]
        period = total_height / (2 * num_slits)  # Height of one segment + one gap

        # Use a fixed x coordinate (centered between start and end x)
        x_coord = (start_point[0] + end_point[0]) / 2

        # Store gap centers for later use
        self.gap_centers = []

        # Create alternating vertical segments and gaps along the y axis
        for i in range(2 * num_slits):
            y_pos = start_point[1] + i * period
            if i % 2 == 0:  # Create solid vertical segment
                seg = Line(
                    start=(x_coord, y_pos, 0),
                    end=(x_coord, y_pos + period, 0),
                    color=WHITE
                )
                grating.add(seg)
            else:  # Store gap center
                gap_center_y = y_pos + period / 2
                self.gap_centers.append((x_coord, gap_center_y, 0))

        return grating

    def construct(self):
        # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))
        # Draw a basic grating
        self.grating_coordinates = ((-2, -2, 0), (-2, 2, 0))
        grating = self.create_grating(*self.grating_coordinates, 5)
        with self.voiceover(text="""
            We are going to derive the formula d sine theta equals n lambda for rays passing through a diffraction grating. <bookmark mark='Title'/>
            First let's create a diffraction grating, where the spacing between the gaps is length d. <bookmark mark='grating'/>
            These rays are going off to the nth bright fringe for in our diffraction pattern, <bookmark mark="rays"/>
            They appear as parallel rays as the distance between the screen and the grating is much greater than the spacing between them. 
            Now if we zoom in on the bottom two rays <bookmark mark="zoom"/>
            If we draw in the first wavefront from the top ray, to where it lines up with the bottom ray. <bookmark mark ="wavefront"/>
            We see that the bottom ray has to travel the length, l, further <bookmark mark="triangle"/>
            For constructive interferance, this path difference has to be a full number of wavelengths, so as this is going to the nth fringe, this l = n lambda, where lambda is the wavelength. <bookmark mark="pathdifference"/>
            Now looking at the triangle we have. <bookmark mark="triangle2"/>
            This angle is the angle between the center of the bright frindge and the grating but also the angle between the wavefront and the grating. <bookmark mark="angle"/>
            The hypotenuse of our triangle is d, the grating spacing. This gives another equation for the length of l, being l = d sine theta. <bookmark mark="trigequation"/>
            If we combine our two formula, we get the equation we want, d sine theta = n lambda. <bookmark mark="finalequation"/>
            Thanks for watching and hopefully this helps. 
            """) as tracker:
            Title = Text("Diffraction Grating", font_size=36).to_edge(UP)
            Title_underline = Underline(Title)
            Title_group = VGroup(Title, Title_underline)
            self.play(Create(Title_group))
            self.wait_until_bookmark ("Title")
            self.play(Create(grating))
            self.wait_until_bookmark ("grating")
            self.wait(2)
            self.dots = []
            # Example of accessing gap centers
            for center in self.gap_centers:
                dot = Dot(point=center, color=RED)
                self.play(Create(dot))
                self.wait(0.5)
                self.dots.append(dot)
            line_length = 10
            theta = 40*DEGREES
            self.rays = []
            for center in self.gap_centers:
                ray = Arrow(center, [center[0] + line_length*np.sin(theta),
                            center[1] + line_length*np.cos(theta), 0], buff=0)
                self.play(Create(ray))
                self.wait(0.5)
                self.rays.append(ray)
            self.wait_until_bookmark ("rays")
            split_length = BraceBetweenPoints(self.rays[0].get_start(), self.rays[1].get_start(),LEFT)
            split_length_label = Text("d", font_size = 15).next_to(split_length,LEFT, buff =0.2)
            self.play(Create(split_length), Write (split_length_label))
            diagram = VGroup(
                grating,
                *self.dots,
                *self.rays,
                split_length,
                split_length_label
                )    
            # Zoom in on the bottom two rays
            self.wait(1)
            bottom_two_rays = VGroup(self.rays[0], self.rays[1])
            # Use camera to zoom in on bottom rays
            self.play(diagram.animate.shift(RIGHT),
                self.camera.frame.animate.scale(0.3).move_to(bottom_two_rays.get_corner(DL)))
            self.wait_until_bookmark ("zoom")
            
            # Calculate intersection point of wavefront with the bottom ray
            # Wavefront starts at gap_centers[1] and goes perpendicular to rays
            # Bottom ray starts at gap_centers[0] and goes at angle theta
            
            # Get actual positions from the shifted rays
            ray0_start = self.rays[0].get_start()
            ray1_start = self.rays[1].get_start()
            
            start_point = ray1_start
            
            # Direction perpendicular to rays (wavefront direction)
            wavefront_dir = np.array([np.cos(theta - np.pi/2), np.sin(theta - np.pi/2), 0])
            
            # Bottom ray start and direction
            ray_start = ray0_start
            ray_dir = np.array([np.sin(theta), np.cos(theta), 0])
            
            # Solve for intersection: start_point + t1*wavefront_dir = ray_start + t2*ray_dir
            # This gives us two equations in two unknowns (t1, t2)
            A = np.column_stack([wavefront_dir[:2], -ray_dir[:2]])
            b = ray_start[:2] - start_point[:2]
            
            try:
                t = np.linalg.solve(A, b)
                t1 = t[0]
                end_point = start_point + t1 * wavefront_dir
            except:
                # Fallback if lines are parallel
                end_point = start_point + line_length * wavefront_dir
            camera_frame = self.camera.frame
            frame_ul = camera_frame.get_corner(UL)
            formula = VGroup(
                MathTex(r"path\ difference\ =n\lambda", font_size = 15),
                MathTex(r"l = n \lambda",font_size = 15),
                MathTex (r"l = d sin \theta", font_size = 15),
                MathTex(r"d sin \theta",r"=",r" n \lambda", font_size = 15)
            ).arrange(DOWN, buff = 0.4).move_to(frame_ul).shift(RIGHT+DOWN)
            
            Wavefront = DashedLine(start_point, end_point)
            self.play(Create(Wavefront))
            self.wait_until_bookmark ("wavefront")
            Side_of_triangle_line = Line(ray0_start, end_point, buff = 0, color = BLUE )
            Side_of_triangle = Brace(Side_of_triangle_line, direction=RIGHT+DOWN, color=BLUE, stroke_width=0.4)
            label = MathTex(r"l", color=BLUE, font_size = 15).next_to(Side_of_triangle, RIGHT+DOWN, buff =0)
            grate_line = Line(ray0_start, ray1_start, buff = 0, color = GREEN ) # line along the grating for drawing arrows
            angle_ray = Angle (Wavefront, grate_line, radius=0.3, other_angle=True, quadrant=(1,-1), color=YELLOW)
            angle_ray_label = MathTex(r"\theta", color=YELLOW, font_size=15).next_to(angle_ray,DOWN, buff=0.2)
            triangle = Polygon(start_point,end_point,ray0_start, color = GREEN).set_opacity(0.4)
            self.play(Create(Side_of_triangle), Create(label))
            self.wait_until_bookmark ("triangle")
            self.play(Write(formula[0]),Write(formula[1]))
            self.wait_until_bookmark ("pathdifference")
            self.play(Create(triangle))
            self.wait_until_bookmark("triangle2")
            self.play(Create(angle_ray), Write(angle_ray_label))
            self.wait_until_bookmark("angle")
            self.play(Write(formula[2]))
            self.wait_until_bookmark("trigequation")
            self.add(formula[2].copy(), formula[1].copy())
            self.play(
                Transform(formula[2], formula[3][0]), 
                Write (formula[3][1]), 
                Transform(formula[1], formula[3][2]) )
            self.wait(5)
            self.play(*[FadeOut(mob) for mob in self.mobjects])