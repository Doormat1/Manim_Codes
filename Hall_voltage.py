from turtle import left
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
import numpy as np


class Hall(ThreeDScene, VoiceoverScene):
    def construct(self):
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))
        with self.voiceover(text="""
                            In this video we will be first understanding where the hall voltage comes from and then using the forces to derive a formula for hall voltage,
                            in terms of magnetic flux density, drift velocity and the thickness of the conductor. <bookmark mark="title"/>
                            Without a magnetic field our charge carriers, here simulated as yellow spheres, pass straight through our rectangular conductor. <bookmark mark="NO_B"/>
                            However once we apply a magnetic field, the charge carries experience the motor effect, so their paths now curve to the top surface where a few get stuck. <bookmark mark="B_field"/>
                            This creates a charge separation betwen the top plates and the bottom plates and this generates an electric field between them <bookmark mark="E_field"/>
                            Now our charge carriers experience two opposing forces, once these are balanced, the charge carriers again pass straight through <bookmark mark="balanced_forces"/>
                            Our charge separation also creates a potential difference between the top and the bottom plates that we can measure with a voltmeter <bookmark mark="voltage"/>
                            To derive our formula, first we write down the forces on our charge carriers. The magnetic force, force = charge times drift velocity times magnetic flux density. <bookmark mark="B_force"/>
                            And our electric force, force = charge times electric field strength. <bookmark mark="E_force"/>
                            As this is the electric field between two parallel plates, the electric field strength = the potential difference across the plates, the hall voltage divided by the distance, d between the plates. <bookmark mark="E_formula"/>
                            So we can change our electric force formula to include this. 
                            Now we can equate these forces as they equal and opposite. <bookmark mark="Equal"/>
                            Cancelling the charges, and rearranging, we get that the hall voltage, VH = B times v times d. <bookmark mark="Final_formula"/> 
                            This means that for a give conductor, normally a semiconductor, the hall voltage is proportional to the magnetic field strength. This makes hall probes very useful for detecting magnetic fields but also measuring changes in position by using a moving magnet. 
                            Thanks for watching and hope these videos help. 

                            """) as tracker:
            Title = Text("Hall Voltage").to_edge(UP)
            Title_underline = Underline(Title)
            title_group = VGroup(Title, Title_underline)
            self.add_fixed_in_frame_mobjects(title_group)
            self.remove(title_group)
            self.play(Write(Title), FadeIn(Title_underline))
            self.wait_until_bookmark("title")
            # Set up 3D camera
            self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
            #add axis to help with directions
            axis = ThreeDAxes().get_axis_labels()
            # Create a flat wireframe cuboid
            # Dimensions: width=6, height=1, depth=4 (flat appearance)
            width, height, depth = 6, 4, 1
            
            # Create the cuboid using Prism (box shape)
            cuboid = Prism(dimensions=[width, height, depth], fill_opacity=0.4)
            cuboid.set_stroke(BLUE, width=2)
            #self.add(axis)
            self.add(cuboid)
            d= Line3D(start=np.array([(1+width)/2, 0, depth/2]), end=np.array([(1+width)/2, 0, -depth/2]), color=WHITE)
            # Position cones at the ends of the line, offset along the line direction
            d_arrow_top = Cone(direction=np.array([0, 0, 1]), height=0.3, base_radius=0.1, color=WHITE).move_to(d.get_start() + np.array([0, 0, 0.15]))
            d_arrow_bottom = Cone(direction=np.array([0, 0, -1]), height=0.3, base_radius=0.1, color=WHITE).move_to(d.get_end() + np.array([0, 0, -0.05]))
            d_label = Text("d", font_size=75, color=WHITE).rotate(PI/2, axis=RIGHT)
            d_label.rotate(PI, Z_AXIS)
            # Position label to the left of the line by moving it to the line's center, then shifting left
            d_label.move_to(d.get_center() + np.array([0.65, 0, 0]))
            self.add(d, d_arrow_top, d_arrow_bottom, d_label)
            # Create spheres that will move along the length (width axis)
            num_spheres = 10
            spheres = VGroup(*[
                Sphere(radius=0.15, resolution=(15, 15))
                .set_color(YELLOW)
                .set_opacity(0.8)
                for _ in range(num_spheres)
            ])
            
            # Position spheres at the starting end (left side)
            start_x = -width / 2
            end_x = width / 2
            
            for i, sphere in enumerate(spheres):
                # Stagger the starting positions
                sphere.move_to([start_x, 
                            np.random.uniform(-height/3, height/3),
                            np.random.uniform(-depth/3, depth/3)])
            
            self.add(spheres)
            self.wait_until_bookmark("NO_B")
            
            # Animate spheres moving along the length
            animations = []
            for sphere in spheres:
                # Each sphere moves from left to right with slight variation
                end_pos = [end_x,
                        np.random.uniform(-height/3, height/3),
                        np.random.uniform(-depth/3, depth/3)]
                animations.append(sphere.animate.move_to(end_pos))
            
            self.play(*animations, run_time=5, rate_func=linear)
            self.wait(2)
            self.play(*[FadeOut(sphere) for sphere in spheres])

                # Create vector field perpendicular to sphere motion (pointing in x-direction)
        # Create vector field perpendicular to sphere motion (pointing in x-direction)
            # The spheres move in z-direction, so vectors point in x-direction
            vector_field = VGroup()
            
            # Create arrows distributed across the x-z plane (horizontal slice)
            num_arrows_x = 5
            num_arrows_z = 3
            arrow_length = 3
            
            for i in range(num_arrows_x):
                for j in range(num_arrows_z):
                    x_pos = -width/2 + (i / (num_arrows_x - 1)) * width
                    z_pos = -depth/2 + (j / (num_arrows_z - 1)) * depth
                    y_pos = 0  # Place them in the middle vertically
                    
                    # Arrows pointing in the positive y-direction (upward, perpendicular to z-motion)
                    arrow = Arrow3D(
                        start=[x_pos, y_pos + arrow_length/2, z_pos],
                        end=[x_pos, y_pos - arrow_length/2, z_pos],
                        color=RED,
                        thickness=0.02,
                        height=0.15,
                        base_radius=0.04
                    )
                    vector_field.add(arrow)
            
            # Add label "B" near the vector field
            b_label = MathTex("\\vec{B}", color=RED, font_size=100)
            b_label.rotate(PI/2, axis=RIGHT) #
            b_label.rotate(PI, Z_AXIS) # Orient for 3D view
            b_label.move_to([0, height/2 + 0.8, 0])
            
            # Fade in the vector field and label
            self.play(FadeIn(vector_field), FadeIn(b_label), run_time=1.5)
            self.wait_until_bookmark("B_field")
            self.wait(0.5)
            

            for i, sphere in enumerate(spheres):
                # Stagger the starting positions
                sphere.move_to([start_x, 
                            np.random.uniform(-height/3, height/3),
                            np.random.uniform(-depth/3, depth/3)])
            #Now animate the spheres with B field applied where some of the electrons do not make it through the conductor
            self.add(spheres)
            back_z = -depth / 2
            front_z = depth / 2
            animations = []
            for i, sphere in enumerate(spheres):
                # Some spheres get stuck partway
                if i < 2:  # First 2 spheres get stuck early
                    stuck_x = np.random.uniform(start_x + 1, start_x + 3)
                elif i < 4:  # Next 2 get stuck later
                    stuck_x = np.random.uniform(start_x + 3, end_x - 1)
                else:  # Last one makes it all the way
                    stuck_x = end_x
                
                # Create curved path to top face (positive z direction)
                start = sphere.get_center()
                end = [stuck_x, np.random.uniform(-height/3, height/3), depth/2]
                
                path = ArcBetweenPoints(start, end, angle=TAU/6)
                animations.append(MoveAlongPath(sphere, path))
            B_Force_arrow = Arrow3D(
                start=cuboid.get_center(),
                end=cuboid.get_center() + [0,0,2],
                resolution=8,
                color= WHITE)
            B_force_label= MathTex(r"F_B", font_size = 100).next_to(B_Force_arrow, LEFT)
            B_force_label.rotate(PI/2, axis=RIGHT) #
            B_force_label.rotate(PI, Z_AXIS) # Orient for 3D view
            self.play(Create(B_Force_arrow), Write(B_force_label), *animations, run_time=4, rate_func=smooth)
            
            #Now we have charge built up on the top face, spheres can now move along the length again. 
            self.wait(2)
            new_spheres = VGroup(*[
                Sphere(radius=0.15, resolution=(15, 15))
                .set_color(YELLOW)
                .set_opacity(0.8)
                for _ in range(num_spheres)
            ])
            for i, new_sphere in enumerate(new_spheres):
                # Stagger the starting positions
                new_sphere.move_to([start_x, 
                            np.random.uniform(-height/3, height/3),
                            np.random.uniform(-depth/3, depth/3)])
        #E_force due to build up of charge on the top plate
            E_Force_arrow = Arrow3D(
                start=cuboid.get_center(),
                end=cuboid.get_center() - [0,0,2],
                resolution=8,
                color= GREEN)
            E_force_label= MathTex(r"F_E", font_size = 100).next_to(E_Force_arrow, RIGHT)
            E_force_label.rotate(PI/2, axis=RIGHT) #
            E_force_label.rotate(PI, Z_AXIS) # Orient for 3D view
            self.play(Create(E_Force_arrow),Write(E_force_label))
            self.wait_until_bookmark("E_field")
            
            # Create voltage measurement lines from top and bottom faces to voltmeter
            # Top face connection point (where spheres accumulated)
            top_point = np.array([0, 0, depth/2])
            # Bottom face connection point
            bottom_point = np.array([0, 0, -depth/2])

            # Voltmeter position (to the right of the cuboid)
            voltmeter_pos = np.array([width/2 + 2, -0.5, 1])

            # Create the voltmeter (circle with V)
            voltmeter_circle = Circle(radius=0.5, color=WHITE)
            voltmeter_circle.rotate(PI/2, axis=RIGHT)  # Orient for 3D view
            voltmeter_circle.move_to(voltmeter_pos)

            v_label = MathTex("V", font_size=60, color=WHITE)
            v_label.rotate(PI/2, axis=RIGHT)
            v_label.move_to(voltmeter_pos)

            voltmeter = VGroup(voltmeter_circle, v_label)

            # # Create connection lines
            # top_line = Line3D(
            #     start=top_point,
            #     end=np.array([voltmeter_pos[0], voltmeter_pos[1], voltmeter_pos[2] + 0.5]),
            #     color=WHITE,
            #     thickness=0.02
            # )

            # bottom_line = Line3D(
            #     start=bottom_point,
            #     end=np.array([voltmeter_pos[0], voltmeter_pos[1], voltmeter_pos[2] - 0.5]),
            #     color=WHITE,
            #     thickness=0.02
            # )
            # Calculate control points for the curve
            start= top_point
            end = np.array([voltmeter_pos[0], voltmeter_pos[1], voltmeter_pos[2] + 0.5])
            mid = (start + end) / 2
                # Offset the midpoint to create the arc
            control = mid + np.array([0.5, 0, 2])  # Adjust offset direction/magnitude

            top_line = CubicBezier(
                start,
                start + (control - start) / 3,
                end + (control - end) / 3,
                end,
                color=WHITE,
                stroke_width=2
            )
            # Bottom arc
            start_bottom = bottom_point
            end_bottom = np.array([voltmeter_pos[0], voltmeter_pos[1], voltmeter_pos[2] - 0.5])
            mid_bottom = (start_bottom + end_bottom) / 2
            # Offset the midpoint to create the arc (same direction as top arc for consistency)
            control_bottom = mid_bottom + np.array([0.5, 0, -2])  # Adjust offset direction/magnitude

            bottom_line = CubicBezier(
                start_bottom,
                start_bottom + (control_bottom - start_bottom) / 3,
                end_bottom + (control_bottom - end_bottom) / 3,
                end_bottom,
                color=WHITE,
                stroke_width=2
            )
            # Animate the appearance of voltmeter and connections
            self.play(
                Create(top_line),
                Create(bottom_line),
                FadeIn(voltmeter),
                run_time=1.5
            )
            self.wait_until_bookmark("voltage")
            self.wait(1)
            self.add(new_spheres)            
            # Animate spheres moving along the length
            animations = []
            for new_sphere in new_spheres:
                # Each sphere moves from left to right with slight variation
                end_pos = [end_x,
                        np.random.uniform(-height/3, height/3),
                        np.random.uniform(-depth/3, depth/3)]
                animations.append(new_sphere.animate.move_to(end_pos))
            
            self.play(*animations, run_time=5, rate_func=linear)
            self.wait(2)

            B_force_formula = MathTex(r"F= Bq \nu_d", font_size=40).to_corner(UR, buff = 1)
            E_force_formula = MathTex(r"F= Eq", font_size=40).next_to(B_force_formula, DOWN, buff=0.5)
            E_force_formula2 = MathTex(r"F= \frac{V_{hall}\ q}{d}", font_size=40).next_to(B_force_formula, DOWN, buff=0.5)
            E_formula = MathTex(r"E = \frac{V_{hall}}{d}", font_size=40).next_to(E_force_formula2, DOWN, buff=0.5)  # Changed to reference E_force_formula2
            Forces_equal = MathTex(r"Bq\nu_d= \frac{V_{hall}\ q}{d}", font_size=40).next_to(E_formula, DOWN, buff=0.5)
            Hall_voltage = MathTex(r"V_{Hall}= B\nu d", font_size=40).next_to(Forces_equal, DOWN, buff=0.5)

            formulas = VGroup(B_force_formula, E_force_formula, E_force_formula2, E_formula, Forces_equal, Hall_voltage)
            self.add_fixed_in_frame_mobjects(formulas)
            self.remove(formulas)

            self.wait_until_bookmark("B_force")
            self.play(Write(B_force_formula))
            self.wait(2)
            self.wait_until_bookmark("E_force")
            self.play(Write(E_force_formula))
            self.wait(2)
            self.wait_until_bookmark("E_formula")
            self.play(Write(E_formula))
            self.wait(2)
            self.play(Unwrite(E_force_formula), Write(E_force_formula2))
            self.wait(2)
            self.wait_until_bookmark("Equal")
            self.play(Write(Forces_equal))
            self.wait(2)
            self.wait_until_bookmark("Final_formula")
            self.play(Write(Hall_voltage))
            self.wait(5)
        
        