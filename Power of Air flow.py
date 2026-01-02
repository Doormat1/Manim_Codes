from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
import numpy as np


class Power(ThreeDScene, VoiceoverScene):
    def construct(self):
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))
        with self.voiceover(text="""
            In this video, we will derive the formula for the power of a wind or water turbine as required for option D of the W J E C A Level Physics Course. <bookmark mark="title"/>
            First, let's imagine our turbine. As the fluid flows through the turbine blades, it describes a cylinder with the same end area as the turbine. <bookmark mark="turbine"/>
            If the fluid is moving with a velocity of v, then each second, the fluid moves a distance of d. This is the length of our cylinder. <bookmark mark="cylindercomplete"/>
            Let's remove the turbine for ease. <bookmark mark="removeturbine"/>
            Our definition of power is the rate of energy transfer. <bookmark mark="power"/>
            Here, the energy is being transferred from the kinetic energy of the fluid. <bookmark mark="kinetic_energy"/>
            So we can substitute this in for energy. <bookmark mark="sub1"/>
            In our formula, we have the mass of the fluid, and this will equal the density times volume. <bookmark mark="3"/>
            The volume of a cylinder is its cross sectional area, A, times its length d. <bookmark mark="4"/>
            So if we insert this into our density formula, we get that the mass equals the density times the area times the length. <bookmark mark="5"/>
            We can now substitute these into our formula for power. <bookmark mark="sub2"/>
            Earlier we stated that the distance d is how far the air moves in a time t. So the velocity of the air is distance divided by time. <bookmark mark="7"/>
            So we can replace the d over t terms in our power formula with v to get our final power formula. The power of a fluid moving through a turbine is one half the density times the cross sectional area times the velocity cubed. <bookmark mark="8"/> 
            Thanks for watching, and I hope this video has helped. 
            """) as tracker:
            Title = Text("Power from Fluid Flow").to_edge(UP)
            Title_underline = Underline(Title)
            title_group = VGroup(Title, Title_underline)
            self.add_fixed_in_frame_mobjects(title_group)
            self.remove(title_group)
            self.play(Write(Title), FadeIn(Title_underline))
            self.wait_until_bookmark("title")
            # Set up 3D camera
            self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
            #add axis to help with directions
            axis = ThreeDAxes()
            axis_labels = ThreeDAxes().get_axis_labels()
            #self.add(axis, axis_labels)
            
            # Create a three-bladed wind turbine
            turbine_blades = VGroup()
            blade_length = 2
            blade_width = 0.3
            num_blades = 3
            
            for i in range(num_blades):
                # Create each blade as a thin rectangle
                blade = Rectangle(width=blade_width, height=blade_length, color=WHITE, fill_opacity=0.7)
                # Rotate blade around origin
                angle = (2 * PI / num_blades) * i
                blade.rotate(angle, axis=X_AXIS)
                blade.rotate(PI/2, axis=X_AXIS)  # Orient blades perpendicular to X-axis
                turbine_blades.add(blade)
            
            # Move turbine blades to the start of the cylinder (x = -3)
            turbine_blades.shift(np.array([3, 0, 0]))
            self.add(turbine_blades)
            
            cylinder = Cylinder(radius=1, height=6, direction=-X_AXIS, show_ends=True, fill_opacity=1)
            cylinder.set_stroke(BLUE, width=2)
            self.add(cylinder)
            
            # Animate turbine rotating as cylinder is created
            self.play(
                Rotate(turbine_blades, angle=2*PI, axis=X_AXIS, rate_func=linear),
                Create(cylinder),
                run_time=3
            )
            self.wait_until_bookmark("turbine")
            
            
            # Add diameter arrow label "d" at the top
            # Cylinder is along X-axis, so diameter arrow should be in Y direction at top (z=3)
            d_arrow = DoubleArrow(
                end=np.array([-2.5, 1, 2]),
                start=np.array([4, 1, 2]),
                color=WHITE,
                buff=0.1
            )
            d_arrow.rotate(-PI/2, axis=X_AXIS)  # Rotate to align with 3D view
            # Anchor 'd' to the arrow in world coordinates, with a small offset:
            d_label = Text("d", font_size=40, color=WHITE)
            # Position d label above the diameter arrow in world coordinates
            d_label.move_to(d_arrow.get_center() + UP * 2)
            # Position 'd' in screen space so it always stays above the arrow and faces the camera
            def _update_d_label(m, dt):
                """Project the arrow endpoints into screen space and place the label
                slightly above the top-most projected endpoint so it sits above the line.
                """
                try:
                    p1 = self.renderer.camera.project_point(d_arrow.get_start())
                    p2 = self.renderer.camera.project_point(d_arrow.get_end())
                    # horizontal position: midpoint of projected endpoints
                    x = (p1[0] + p2[0]) / 2
                    # vertical position: slightly above the top endpoint
                    y = max(p1[1], p2[1]) + 0.06
                    m.move_to(np.array([x, y, 0]))
                except Exception:
                    pass
            d_label.add_updater(_update_d_label)

            # Add front face label "A"
            # Anchor 'A' to the cylinder front face (or wherever you want relative to cylinder):
            a_label = Text("A", font_size=50, color=WHITE)
            # Place A next to the circular face at the start of the cylinder
            a_label.move_to(cylinder.get_right() + RIGHT * 0.4)
            # Position 'A' in screen space so it stays beside the front face and faces the camera
            def _update_a_label(m, dt):
                """Project the cylinder front face point into screen space and position
                the label just to the right of it in screen coordinates.
                """
                try:
                    proj = self.renderer.camera.project_point(cylinder.get_right())
                    # small rightward offset in screen space
                    m.move_to(np.array([proj[0] + 0.06, proj[1], 0]))
                except Exception:
                    pass
            a_label.add_updater(_update_a_label)
            self.wait_until_bookmark("cylindercomplete")
            self.play(FadeOut(turbine_blades))
            # Add labels as fixed-in-frame mobjects (they are positioned each frame by updaters)
            self.add_fixed_in_frame_mobjects(d_label, a_label)
            self.play(Create(d_arrow), Write(d_label), Write(a_label), run_time=2)
            airmove = VGroup(cylinder, d_arrow)
            Power_formula = MathTex(r"\frac{\Delta E}{\Delta t}")                       #0
            Kinetic_energy_formula=MathTex(r"\frac{1}{2}mv^2")                          #1
            Power_formula_sub=MathTex(r"\frac{1}{2} \frac{mv^2}{\Delta t}")             #2
            Density = MathTex(r"m = \rho V")                                            #3
            Volume = MathTex(r"V = Ad")                                                 #4
            mass = MathTex(r"m =\rho Ad ")                                              #5
            Power_formula_sub2 = MathTex(r"\frac{1}{2} \frac{\rho A d v^2}{\Delta t}")  #6
            velocity = MathTex(r"v= \frac{d}{t}")                                       #7
            Power_final = MathTex(r"\frac{1}{2} \rho A v^3")                            #8
            formulas= VGroup(Power_formula, Kinetic_energy_formula, Power_formula_sub, Density, Volume, mass, Power_formula_sub2, velocity, Power_final).arrange(DOWN, aligned_edge = LEFT).to_corner(UL)
            for formula in formulas:
                formula.font_size = 36 
            
            self.play(airmove.animate.shift(np.array([-4,2,0])))
            self.wait_until_bookmark("removeturbine")
            self.add_fixed_in_frame_mobjects(formulas)
            self.remove(formulas)
            formulas[2].move_to(formulas[0])
            self.wait_until_bookmark("power")
            self.play(Write(formulas[0]))
            self.wait_until_bookmark("kinetic_energy")
            self.play(Write(formulas[1]))
            self.wait_until_bookmark("sub1")
            self.play(Unwrite(formulas[0]), Write(formulas[2]))
            self.play(FadeOut(formulas[1]))
            self.wait_until_bookmark("3")
            for x in range(3,6):
                formulas[x].next_to(formulas[x-1], DOWN)
                self.play(Write(formulas[x]))
                if x < 5:  # Wait for bookmarks 4 and 5, but not after the last one
                    self.wait_until_bookmark(str(x + 1))
            self.wait_until_bookmark("sub2")
            formulas[6].move_to(formulas[2])
            self.play(Unwrite(formulas[2]), Write(formulas[6]))
            for x in range(3,6):
                self.play(FadeOut(formulas[x]))
            self.wait_until_bookmark("7")
            for x in range(7,9):
                formulas[x].next_to(formulas[x-1], DOWN)
                self.play(Write(formulas[x]))
                if x < 8:  # Wait for bookmark 8, but only once
                    self.wait_until_bookmark(str(x + 1))
            self.wait_until_bookmark("8")
            self.wait(5)
