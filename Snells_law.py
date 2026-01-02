from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
import numpy as np

class Snells(VoiceoverScene):
    def construct(self):
         # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))
        with self.voiceover(text ="""
            In this video, we are going to first establish Snell's law for refraction by looking at the geometry involved in a wave changing medium and then we will use this law to derive the equation for the critical angle of a medium
        """ ) as tracker:
            title= Text("Deriving Snells Law", font_size=36).to_edge(UP)
            underline = Underline (title)
            self.play(Write (title), Write(underline))
            self.wait(2)
        #Drawing two wave fronts showing refraction with wavefronts 
        medium_1 = Rectangle(color = BLUE, height= 4, width= 20).to_edge(DOWN).set_opacity(0.50)   # Use a box of different colour to show the change in medium
        n = 1.6 #refractive index of our material
        line_length = 5   # set the length of the wavefronts
        angle= 30/360 * 2*np.pi  #angle of incidence in degrees with conversion to radians
        angle2= np.arcsin(np.sin(angle)/n)
        y= medium_1.get_top()[1]
        x= 0-line_length*np.cos(angle)/2
        wavefront_1 = Line([x,y,0], [x+line_length*np.cos(angle),y+line_length*np.sin(angle),0], color = GREEN)       #wavefront just meeting the medium
        perpendicular_distance_medium = (line_length) * np.sin(angle2)
        
        wavefront_2 = Line([x + perpendicular_distance_medium * np.sin(angle), 
                    y - perpendicular_distance_medium * np.cos(angle), 0],
                   [x +perpendicular_distance_medium * np.sin(angle)+ line_length*np.cos(angle2), y, 0], 
                   color=GREEN)
        air_triangle = Polygon(
            wavefront_1.get_start(),
            wavefront_1.get_end(),
            wavefront_2.get_end(),
            color=YELLOW,
            stroke_width=0,
            fill_opacity=0.25
            )
        water_triangle = Polygon(
            wavefront_1.get_start(),
            wavefront_2.get_start(),
            wavefront_2.get_end(),
            color=PURPLE,
            stroke_width=0,
            fill_opacity=0.3
            )   
        distance_1= DoubleArrow (wavefront_1.get_start(),wavefront_2.get_start(), buff = 0, stroke_width = 3, tip_length = 0.2)  #distance wave travels in the medium in time t
        distance_2 = DoubleArrow(wavefront_1.get_end(), wavefront_2.get_end(), buff = 0, stroke_width=3, tip_length = 0.2)  #distance wave travels in air in time t
        distance_1_label = MathTex(r"\lambda_2", font_size = 25).next_to(distance_1, LEFT, buff = 0.2)
        distance_2_label = MathTex(r"\lambda_1", font_size = 25).next_to(distance_2, RIGHT, buff = 0.2)
        distance_1_label_speed = MathTex(r"c_2 t", font_size = 25).next_to(distance_1, LEFT, buff = 0.2)
        distance_2_label_speed = MathTex(r"c_1 t", font_size = 25).next_to(distance_2, RIGHT, buff = 0.2)
        distance_1_label_triangle = MathTex(r"c_2 t = l sin \theta_2", font_size = 25).next_to(distance_1, LEFT, buff = 0.2)
        distance_2_label_triangle = MathTex(r"c_1 t = l sin \theta_1", font_size = 25).next_to(distance_2, RIGHT, buff = 0.2)
        top_edge = Line(
        wavefront_1.get_start(),
        wavefront_2.get_end(),
        color= PURPLE,
        buff = 0
        )
        top_edge_label =MathTex("l", font_size= 30, color = PURPLE).next_to(top_edge,UP, buff= 0.2).shift(RIGHT)
        angle_1 =Angle(
            wavefront_1,
            top_edge,
            radius = 1,
            color = WHITE,
            other_angle=True
            )
        angle_2 =Angle(
            wavefront_2,
            top_edge,
            radius = 1,
            color = WHITE,
            other_angle=True,
            quadrant= (-1,-1)
            )
        angle_1_label = MathTex(r"\theta_1", font_size = 25).next_to(angle_1, RIGHT, buff = 0.2)
        angle_2_label = MathTex(r"\theta_2", font_size = 25).next_to(angle_2, LEFT, buff = 0.2)
        normal = DashedLine(
            [x+line_length/(2*np.cos(angle)), top_edge.get_midpoint()[1]-1.5, 0],
            [x+line_length/(2*np.cos(angle)), top_edge.get_midpoint()[1]+1.5, 0], 
            color=WHITE, buff=0
            )
        ray_air = Arrow(wavefront_1.get_midpoint(), normal.get_center(), color = WHITE, buff=0, stroke_width=3, tip_length = 0.1)
        ray_water = Arrow(normal.get_center(),wavefront_2.get_midpoint(), color = WHITE, buff = 0, stroke_width=3, tip_length = 0.1)
        normal_bottom = Line(normal.get_center(), 
                             normal.get_start())
        normal_angle_air = Angle(ray_air, normal, radius = 1, other_angle=True, color = WHITE, quadrant=(-1,1))      
        normal_angle_air_label = MathTex(r"\theta_1", font_size = 25).next_to(normal_angle_air,UP, buff = 0.2)
        normal_angle_water = Angle(normal_bottom, ray_water, radius = 0.5, other_angle=False, color = WHITE)      
        normal_angle_water_label = MathTex(r"\theta_2", font_size = 25).next_to(normal_angle_water, DOWN + RIGHT, buff = 0.2)
        formula1 = MathTex(r"c_1 t = l sin \theta_1", font_size =35).to_corner(UL, buff = 1)
        formula2 = MathTex(r"c_2 t = l sin \theta_2", font_size =35).next_to(formula1, DOWN, buff = 0.2)
        refractive_index = MathTex (r"n = \frac{c_1}{c_2}", font_size = 35).next_to(formula2, DOWN, buff = 0.2)
        refractive_index_sub = MathTex (r"n = \frac{l t sin \theta_1}{l t sin \theta_2}", font_size = 35).next_to(formula2, DOWN, buff = 0.2)
        snells_law = MathTex (r"sin \theta_1 = n sin \theta_2", font_size = 35).next_to(refractive_index_sub, DOWN, buff = 0.2)
        with self.voiceover(text = """Here we have a change in medium for our wave, where the blue area makes the wave move slower. <bookmark mark="medium"/>
                            As our wave moves from one medium to the other, it bends towards the normal. <bookmark mark ="normalline"/>
                            If we now draw in two consecutive wave fronts. The first is just as the wave is touching the boundary. <bookmark mark ="wavefront1"/>
                            The second is the previous wavefront, the first that is wholely in the slower medium.<bookmark mark ="wavefront2"/>
                            Now lets label our angles. The angle from the normal line and the incident ray, this is the same as the angle between the wavefront and the medium. This we will call theta 1. <bookmark mark ="theta1" />
                            The angle between our refracted ray and the normal line, this is the same as the angle between the wavefront in the slower medium and the boundary. We will call this theta 2. <bookmark mark ="theta2" />
                            As these are two consecutive waves, the distance between them is equal to the wavelength. So this distance is the wavelength in the faster medium. <bookmark mark ="distance1"/>
                            And this distance is the wavelength in the slower medium. <bookmark mark ="distance2"/>
                            These distances are both equal to the speed of the wave times the time taken to travel this distance. <bookmark mark ="speed"/>
                            Now lets consider some triangles. 
                            We have the yellow triangle formed by our wavefront in the faster medium and the medium boundary. <bookmark mark ="yellow_triangle"/>
                            And the purple triangle formed by our wavefront in the slower medium and the medium boundary. <bookmark mark ="purple_triangle"/>
                            Both triangles share the same hypotenuse, which we have labelled l. <bookmark mark ="hyp_l"/>
                            Using trignonmetry, we can also define our two distances as l sine theta 1 and l sine theta 2. <bookmark mark ="redefinedistance"/>
                            The refractive index of a medium is defined as the ratio of the speed outside and inside the medium.<bookmark mark ="refractiveindex"/>
                            Next we can substitute in our distances for the values of c 1 and c 2. <bookmark mark ="refractive_subin"/>
                            From here we rearrange to make sine theta 1 the subject and we get Snell's Law. 
                            """) as tracker:        
            self.play(Create (medium_1))            
            self.wait_until_bookmark ("medium")
            self.play (Create (ray_air), Create (ray_water), Create (normal))
            self.wait_until_bookmark ("normalline")
            self.play(Create (wavefront_1))
            self.wait_until_bookmark("wavefront1")
            self.play(Create (wavefront_2))
            self.wait_until_bookmark("wavefront2")
            self.play(Create (angle_1), Create (normal_angle_air), Write (angle_1_label), Write (normal_angle_air_label))
            self.wait_until_bookmark ("theta1")
            self.play(Create (angle_2), Create (normal_angle_water), Write (angle_2_label), Write (normal_angle_water_label))
            self.wait_until_bookmark ("theta2")
            self.play(Create (distance_2), Write (distance_2_label))
            self.wait_until_bookmark ("distance1")
            self.play(Create (distance_1), Write (distance_1_label))
            self.wait_until_bookmark ("distance2")
            self.play(Transform(distance_1_label,distance_1_label_speed), Transform(distance_2_label, distance_2_label_speed))
            self.wait_until_bookmark ("speed")
            self.play(Create(air_triangle))
            self.wait_until_bookmark ("yellow_triangle")
            self.play(Create(water_triangle))
            self.wait_until_bookmark ("purple_triangle")
            self.play(Create(top_edge), Write (top_edge_label))
            self.wait_until_bookmark ("hyp_l")
            self.play(ReplacementTransform(distance_1_label, distance_1_label_triangle), 
                      ReplacementTransform(distance_2_label, distance_2_label_triangle))
            self.play(Write (formula1), Write (formula2))
            self.wait_until_bookmark ("redefinedistance")
            self.play(Write(refractive_index))
            self.wait_until_bookmark ("refractiveindex")
            self.play(Transform(refractive_index, refractive_index_sub))
            self.wait_until_bookmark ("refractive_subin")
            self.play(Write(snells_law))
            self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
#Now move onto the critical angle
        ray_length = 2   #use this to change the length of the rays in the critical angle animation
        # Initial and final angles
        initial_angle = 25/360 * 2*np.pi
        critical_angle_final = np.arcsin(1/n)-0.000000001  # When refraction = 90°, sin(θ_c) = 1/n

        # Create ValueTracker for the incident angle
        angle_tracker = ValueTracker(initial_angle)

        # Create static objects
        critical_angle_title = Text("Deriving for the Critical Angle", font_size=36).to_edge(UP)
        underline2 = Underline(critical_angle_title)
        out_normal = DashedLine(
            [top_edge.get_midpoint()[0], top_edge.get_midpoint()[1]-1.5, 0],
            [top_edge.get_midpoint()[0], top_edge.get_midpoint()[1]+1.5, 0]
        )
        #Create the right angle symbol
        right_angle = Square(0.2, color =WHITE).next_to(top_edge.get_midpoint(),UP+RIGHT,buff= 0)
        # Create dynamic objects that will update
        ray_water_out = always_redraw(lambda: Arrow(
            [top_edge.get_midpoint()[0] - ray_length*np.sin(angle_tracker.get_value()),
            top_edge.get_midpoint()[1] - ray_length*np.cos(angle_tracker.get_value()), 0],
            top_edge.get_midpoint(), 
            buff=0, stroke_width=2, tip_length=0.3
        ))

        ray_air_out = always_redraw(lambda: Arrow(
            top_edge.get_midpoint(),
            [top_edge.get_midpoint()[0] + ray_length*np.sin(np.arcsin(np.sin(angle_tracker.get_value())*n)),
            top_edge.get_midpoint()[1] + ray_length*np.cos(np.arcsin(np.sin(angle_tracker.get_value())*n)), 0],
            buff=0, stroke_width=2, tip_length=0.3
        ))

        out_incident_angle = always_redraw(lambda: Angle(
            Line(
                [top_edge.get_midpoint()[0] - ray_length*np.sin(angle_tracker.get_value()),
                top_edge.get_midpoint()[1] - ray_length*np.cos(angle_tracker.get_value()), 0],
                top_edge.get_midpoint()
            ),
            out_normal,
            radius=1,
            quadrant=(-1, -1)
        ))
        out_normal_top = Line (out_normal.get_center(),out_normal.get_end())
        out_refracted_angle = always_redraw(lambda: Angle(
                ray_air_out,
            out_normal_top,
            radius=1,
            quadrant = (1,1),
            other_angle=False
        ))
        snells_law_reversed1 = MathTex(r"n sin\ \theta_1 = sin\ \theta_2", font_size = 30).to_corner(UL, buff = 1)
        snells_law_reversed2 = MathTex(r"n sin\ \theta_c = sin\ 90", font_size = 30).next_to(snells_law_reversed1, DOWN, buff = 0.2)
        snells_law_reversed3 = MathTex (r"n sin\ \theta_c = 1", font_size = 30).next_to(snells_law_reversed2, DOWN, buff = 0.2)
        snells_law_reversed4 = MathTex(r"\theta_c = sin^{-1} ( \frac{1}{c})", font_size = 30).next_to(snells_law_reversed3, DOWN, buff = 0.2)
        # Animation sequence
        with self.voiceover(text="""
                    Now if we reverse our wave, so that is moving from the slower medium, to a faster one. <bookmark mark="otherway"/>
                    We can see here that as our wave speeds up it bends away from the normal. <bookmark mark="ninety"/>
                    Eventually our refracted angle reaches ninety degrees. After this our wave will then undergo total internal reflection rather than refracting out. 
                    Now lets look at the forumlas behind this. <bookmark mark ="formula1"/>
                    We've swapped theta 1 and 2 compared to the formula before to keep the same value of the refractive index as this is what many questions will expect. <bookmark mark ="formula2"/>
                    When we reach the critical angle, theta c. The refacted angle becomes 90 degrees. <bookmark mark="formula3"/>
                    And sine of 90, is 1. <bookmark mark ="formula4"/>
                    Now we can rearrange to get theta c. 
                    So the critical angle of a material is equal to inverse sine of one over the refractive index. This means that materials with a higher refractive index have a lower critical angle. 
                            """)as tracker:
            self.play(Write(critical_angle_title), Write(underline2))
            self.play(Create(medium_1))
            self.wait_until_bookmark ("otherway")      
            self.play(Create(ray_water_out))
            self.play(Create(ray_air_out))
            self.play(Create(out_normal))
            self.play(Create(out_incident_angle))
            self.play(Create(out_refracted_angle))
            self.wait_until_bookmark ("ninety")
            # Animate the angle changing
            self.play(
                angle_tracker.animate.set_value(critical_angle_final),
                run_time=3,
                rate_func=smooth
            )
            self.play(FadeOut(out_refracted_angle),FadeIn(right_angle))
            self.wait_until_bookmark ("formula1")
            self.play(Write (snells_law_reversed1))
            self.wait_until_bookmark ("formula2")
            self.play(Write (snells_law_reversed2))
            self.wait_until_bookmark ("formula3")
            self.play(Write (snells_law_reversed3))
            self.wait_until_bookmark ("formula4")
            self.play(Write (snells_law_reversed4))
            self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        with self.voiceover(text="""
             So in summary, we derived Snells law, <bookmark mark="title"/> as  sine theta 1 = n sine theta 2, where n is the refractive index of the slower medium, where theta 2 is.
            And then we have used this to derive the equation for the critical angle of the slower medium.
            <bookmark mark="critical"/>
            Here the critical angle is the inverse sine of the 1 over the refractive index. 
            Thanks for watching and hopefully this has helped.  
            
                            """)as tracker:
            summary_title = Text ("In Summary", font_size=36).to_edge(UP)
            summary_underline = Underline(summary_title)
            summary1 = MathTex(r"sin\ \theta_1\ =n \ sin\ \theta_2").next_to(summary_underline, DOWN, buff = 2)
            summary2 = MathTex(r"\theta_c\ =\ sin^{-1} \frac{1}{n}").next_to(summary1, DOWN, buff = 0.5)

            self.play(Write (summary_title),  Create(summary_underline))
            self.wait_until_bookmark ("title")
            self.play(Write(summary1))
            self.wait_until_bookmark("critical")
            self.play(Write(summary2))
            self.wait(5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        