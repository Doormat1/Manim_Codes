from pkgutil import extend_path
from glm import e
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService           
import os
import numpy as np


class shm(VoiceoverScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_mobject = None
    
    def add_below(self, mobject, buff=0.3):
        if self.last_mobject is None:
            mobject.to_edge(UP)
        else:
            mobject.next_to(self.last_mobject, DOWN, buff=buff)
        self.play(Create(mobject))
        self.last_mobject = mobject
        return mobject
    
    def construct(self):
                 # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))
        #SHM condition outline and example equations for x, v and a
        shm_title = Text("Deriving SHM Equations", font_size=36).to_edge(UP)
        shm_underline = Underline(shm_title)
        shm_title_group = VGroup(shm_title, shm_underline)
        shm_condition = MathTex(r"x \propto -a").next_to(shm_title_group,DOWN,buff =0.2)
        shm_displacement = MathTex(r"x = A \sin \omega t ")
        velocity_definition = MathTex(r"v= \frac{dx}{dt}")
        shm_velocity = MathTex(r"v= A \omega \cos \omega t")
        accelearation_definition = MathTex(r"a= \frac{dv}{dt}")
        shm_acceleration = MathTex(r"a = - A \omega^2 \sin \omega t")
        shm_acceleration2 = MathTex(r"a = - c x")
        shm_condition2 = MathTex(r"x \propto -a").next_to(shm_title_group,DOWN,buff =0.2)
        with self.voiceover(text="""
            In this video we will be deriving equations for simple harmonic motion, or SHM. 
            Lets first look at the general condition for SHM. 
            For SHM to occur, the displacement of the object must be directly proportional to the negative of its acceleration. <bookmark mark="displacement"/>
            Lets have a guess at an equation for the displacement of an object undergoing SHM. <bookmark mark="guess"/>
            As we know we have periodic motion, perhaps a sine wave is a good idea to try. 
            So if we have a particle moving with an amplitude of A, and an angular frequency of omega, our displacement at time t will be A! sine omega t. <bookmark mark="dxdt"/>
            Velocity is the rate of change of displacement, <bookmark mark="velocity"/> so we if we differentiate an equation for displacement, we will get an equation for velocity. <bookmark mark="differentiate"/>
            Using chain rule, we differentiate the inside of the equation first, so this gives us an omega term. If we then differentiate the outside, we get cosine. 
            Giving us a formula for velocity, v equals A omega cosine omega t. <bookmark mark="dvdt"/>
            If we continue our differentiation, we get an equation for acceleration. <bookmark mark="acceleration"/>
            Again using the chain rule, we differentiate the inside first, giving us another omega term. Then differentiating the outside, we get negative sine. 
            Giving us a formula for acceleration, a equals negative A omega squared sine omega t. <bookmark mark="substitute"/>
            Now if we look back at our original equation for displacement, we can substitute this into our equation for acceleration.
            This gives us a final equation for acceleration, a equals negative c times x, where c is omega squared. <bookmark mark="final"/> 
            """)as tracker:
            
            self.add_below(shm_title_group)
            self.wait(2)
            self.add_below(shm_condition)
            self.wait_until_bookmark("guess")
            self.add_below(shm_displacement)
            self.wait_until_bookmark("dxdt")
            self.add_below(velocity_definition)
            self.wait_until_bookmark("velocity")
            self.add_below(shm_velocity)
            self.wait_until_bookmark("acceleration")
            self.add_below(accelearation_definition)
            self.wait(2)
            self.add_below(shm_acceleration)
            self.wait(2)
            self.play(shm_displacement.animate.set_color(YELLOW))
            self.wait(2)
            self.add_below(shm_acceleration2)
            self.wait(2)
            self.add_below(shm_condition2)
            self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)

        #Now move on to pendulum
        
        Pendulum_string = Line([0,2,0],[0,0,0])
        Pendulum_bob = Circle(0.5, fill_opacity=1).move_to([0, -0.5, 0])
        Pendulum = VGroup(Pendulum_string, Pendulum_bob)
 
        with self.voiceover(text="""
            Now lets look at an example of SHM in practice, the simple pendulum, a heavy weight on a length of light, inextensible string. <bookmark mark='intro'/>
            If we look at the forces acting on our pendulum. <bookmark mark='forces'/>
            The weight of pendulum creates a downwards force, the vertical component of which is opposed by the tension. <bookmark mark='tension'/>
            So the tension in the string equals m g cos theta. 
            This also creates a restoring force back towards the equilibrium point. This restoring force is m g sine theta.<bookmark mark='tension_eq'/>
            Now lets define some distances on our pendulum. <bookmark mark='distances'/>
            The length of our pendulum, is measured from the pivot to the centre of mass, here the centre of our pendulum bob. <bookmark mark='length'/>
            The displacement of our pendulum is measured from the equilibrium point to the centre of mass again.
            For convenience later we are going to define this displacement as a negative value, as it is in the opposite direction to the force we have already defined. <bookmark mark='displacement'/>
            Now lets use these forces and displacements to derive an equation for the time period of a pendulum. <bookmark mark='derive'/>
            We have our equation for restor ing force, F = - m g sine theta.
            We are now going to use the small angle approximation, which states that for small angles, sine theta is approximately equal to theta,
            to simplify our equation. <bookmark mark='small_angle'/>
            So we can substitute this into our equation for force, giving us F = - m g theta.
            As our pendulum swings, the bob traces out an arc, the length of this arc is equal to the radius l, times the angle theta in radians.
            So we can rearrange this to give us theta equals x over l. <bookmark mark='theta_eq'/>
            We can now substitute this into our equation for force, giving us F = - m g x over l.<bookmark mark='force_eq'/>
            Lets clear some old equations up and now look back at our definition for shm, x equals negative omega squared a, where a is the acceleration.
            Applying Newton's second law, a equals F over m, we can substitute this into our equation for displacement, giving us x equals negative omega squared F over m. <bookmark mark="substitute"/>
            Now we have two equations for force, so we can set them equal to each other. <bookmark mark="force"/>
            """)as tracker:
            self.play(Create(Pendulum))
            self.wait(2)

            pivot_point = Pendulum_string.get_start()

            # Swing right
            self.play(
                Rotate(Pendulum, angle=30*DEGREES, about_point=pivot_point, axis=OUT),
                rate_func=smooth,
                run_time=1
            )

            for _ in range(3):
                # Swing left
                self.play(
                    Rotate(Pendulum, angle=-60*DEGREES, about_point=pivot_point, axis=OUT),
                    rate_func=smooth,
                    run_time=1
                )
                # Swing right
                self.play(
                    Rotate(Pendulum, angle=60*DEGREES, about_point=pivot_point, axis=OUT),
                    rate_func=smooth,
                    run_time=1
                )
                                # Now add force arrows
            weight = Arrow(Pendulum_bob.get_center(), Pendulum_bob.get_center()-[0,2,0])
            weight_label = Text ("mg").next_to(weight, DOWN)
            equilibrium_line = DashedLine(Pendulum_string.get_start(), Pendulum_string.get_start()-[0,3,0])
            theta = Angle(Pendulum_string, equilibrium_line, other_angle=True, radius=1)
            theta_label = MathTex(r"\theta", font_size = 20).next_to(theta, DOWN, buff=0)
            pendulum_length = Line(Pendulum_string.get_start(), Pendulum_bob.get_center(), buff = 0)
            # Create the brace for the pendulum string
            length_brace = Brace(pendulum_length, direction=LEFT)
            length_label = length_brace.get_text("length, l")

            # Get the angle of the pendulum string
            string_angle = Pendulum_string.get_angle()

            # Rotate both the brace and label around the midpoint
            midpoint = Pendulum_string.get_center()
            length_brace.rotate(string_angle - PI/2, about_point=midpoint)
            length_label.rotate(string_angle + PI/2, about_point=midpoint)

            # Adjust label position if needed
            length_label.next_to(length_brace, direction=RIGHT, buff=0.1).shift(UP)

            length = VGroup(length_brace, length_label)
            displacement_line = Line([0,3,0],Pendulum_bob.get_center(), buff = 0)
            displacement= BraceLabel(displacement_line, "-x",DOWN).shift(DOWN)
            tension = LabeledArrow( MathTex(r"T = mg\ cos\ \theta", font_size = 20), start= Pendulum_bob.get_center(), end = Pendulum_string.get_center(), label_position=0.6)
            tension.label.rotate(angle=30*DEGREES)
            restoring_force = LabeledArrow(MathTex(r"F = -mg\ sin \theta", font_size = 20), start = Pendulum_bob.get_center(), end = Pendulum_string.get_center(), label_position=0.6).rotate(PI/2, about_point=Pendulum_bob.get_center())
            restoring_force.label.rotate(angle=-60*DEGREES).shift(DOWN*0.5)
            Pendulum_derivation = VGroup(
                    MathTex(r"F = -mg\ \sin \theta"), #0
                    MathTex(r"\sin \theta = \theta"), #1
                    MathTex(r"F=-mg\theta"), #2
                    MathTex(r"x = l \times \theta"),#3
                    MathTex(r"\theta = \frac{x}{l}"),#4
                    MathTex(r"F=-mg \frac{x}{l}"), #5
                    MathTex(r"x = - \omega^2 a"), #6
                    MathTex(r"a = \frac{F}{m}"),#7
                    MathTex(r"x = - \omega^2 \frac{F}{m}"), #8
                    MathTex(r"F = - \frac{xm}{\omega^2}"), #9
                    MathTex(r"-\frac{xm}{\omega^2} = -mg \frac{x}{l}"), #10
                    MathTex(r"\frac{1}{\omega^2} = \frac{g}{l}"), #11
                    MathTex(r"\omega = \frac{2\pi}{T}"), #12
                    MathTex(r"T = 2\pi \sqrt{\frac{l}{g}}") #13
                ).arrange(DOWN, buff=0.4).to_corner(UL)    
            self.wait_until_bookmark("intro")
            self.play(Create(equilibrium_line), Create(theta), Write(theta_label))
            self.play(Create(weight), Write(weight_label))
            self.wait_until_bookmark("forces")
            self.play(Create(tension))
            self.wait_until_bookmark("tension")
            self.play(Create(restoring_force))
            self.wait_until_bookmark("tension_eq")
            self.play(Create(length))
            self.wait_until_bookmark("length")
            self.play(Create(displacement))
            self.wait_until_bookmark("derive")
            self.play(Write(Pendulum_derivation[0]))
            self.play(Write(Pendulum_derivation[1]))
            self.wait_until_bookmark("small_angle")
            self.play(Write(Pendulum_derivation[2]))
            self.play(Write(Pendulum_derivation[3]))
            self.wait_until_bookmark("theta_eq")
            for n in range (13,3,-1):   #move all the other parts of the VGroup up one to allow for the transform coming up 
                Pendulum_derivation[n].move_to(Pendulum_derivation[n-1])
            
            self.play(TransformMatchingTex(Pendulum_derivation[3],Pendulum_derivation[4]))
            
            self.play(Write(Pendulum_derivation[5]))
            self.wait_until_bookmark("force_eq")
            self.play(*[FadeOut(Pendulum_derivation[n]) for n in range (0,5)if n != 3], Pendulum_derivation[5].animate.to_corner(UL))
            Pendulum_derivation[6].move_to(Pendulum_derivation[1])
            for n in range (6,8):   #move all the other parts of the VGroup up one to allow for the transform coming up 
                Pendulum_derivation[n].next_to(Pendulum_derivation[n-1], DOWN, buff = 0.4)
            self.play(Write(Pendulum_derivation[6]))
            self.play(Write(Pendulum_derivation[7]))
            self.wait_until_bookmark ("substitute")
            Pendulum_derivation[8].move_to(Pendulum_derivation[6])
            self.play(Transform(Pendulum_derivation[6],Pendulum_derivation[8]))
            self.wait(2)
            Pendulum_derivation[9].move_to(Pendulum_derivation[6])
            self.play(Transform(Pendulum_derivation[6],Pendulum_derivation[9]))
            Pendulum_derivation[10].next_to(Pendulum_derivation[6], DOWN, buff=0.4)
            self.play(FadeOut(Pendulum_derivation[7]), Write(Pendulum_derivation[10]))
            self.wait_until_bookmark ("force")
            self.play(FadeOut(Pendulum_derivation[5],Pendulum_derivation[6]), Pendulum_derivation[10].animate.to_corner(UL))
            for n in range (11,14):   #move all the other parts of the VGroup to realign
                Pendulum_derivation[n].next_to(Pendulum_derivation[n-1], DOWN, buff = 0.4)

        with self.voiceover(text="""
            Rearranging this equation to make omega the subject, we get one over omega squared equals g over l. <bookmark mark='omega'/>
            Now we can substitute omega equals 2 pi over T, <bookmark mark='period'/>
            and rearrange to get our final equation for the time period of a simple pendulum, T equals 2 pi root l over g. <bookmark mark='final'/>
            """) as tracker:
            self.play(Write(Pendulum_derivation[11]))
            self.wait_until_bookmark("omega")
            self.play(Write(Pendulum_derivation[12]))
            self.wait_until_bookmark("period")
            self.play(Write(Pendulum_derivation[13]))
            self.wait_until_bookmark("final")
            self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects]) #fade out all mobjects at end of scene ready for springs

        self.wait(2)
        #Now move on to springs
        
# Fixed ceiling support
        ceiling = Line(LEFT * 2, RIGHT * 2, stroke_width=8)
        ceiling.to_edge(UP, buff=0.5)
        
        # Hatch marks for ceiling
        hatches = VGroup(*[
            Line(ORIGIN, DOWN * 0.2).shift(ceiling.get_start() + RIGHT * i * 0.2)
            for i in range(21)
        ])
        
        # Spring parameters
        spring_coils = 15
        spring_width = 0.3
        equilibrium_length = 3
        
        def create_spring(length, anchor_point):
            """Create a spring with given length attached to anchor point"""
            points = []
            for i in range(spring_coils * 4 + 1):
                t = i / (spring_coils * 4)
                x = spring_width * np.sin(i * PI / 2) if i % 2 else -spring_width * np.sin(i * PI / 2)
                y = -t * length
                points.append(anchor_point + np.array([x, y, 0]))
            
            spring = VMobject()
            spring.set_points_as_corners(points)
            spring.set_stroke(BLUE, width=3)
            return spring
        
        # Anchor point for spring (bottom of ceiling)
        anchor = ceiling.get_center() + DOWN * 0.1
        
        # Initial spring at equilibrium
        spring = create_spring(equilibrium_length, anchor)
        
        # Mass (square block)
        mass = Square(side_length=0.6, fill_color=RED, fill_opacity=1, stroke_color=WHITE, stroke_width=2)
        mass.move_to(spring.get_end())
        
        # Equilibrium line
        equilibrium_y = spring.get_end()[1]
        eq_line = DashedLine(LEFT * 1.5, RIGHT * 1.5, stroke_width=2, color=GREEN)
        eq_line.move_to(anchor + DOWN * equilibrium_length)
        eq_label = Text("Equilibrium", font_size=24, color=GREEN).next_to(eq_line, RIGHT, buff=0.2)
        
        # Add initial objects
        self.add(ceiling, hatches, spring, mass, eq_line, eq_label)
        self.wait(0.5)
        
        # Oscillation parameters
        amplitude = 1.5  # Initial amplitude
        damping = 0.15   # Damping factor
        frequency = 1  # Oscillation frequency
        duration = 6     # Total oscillation time
        final_offset = 1  # How far below equilibrium to finish
        
        def get_position(t):
            """Calculate damped oscillation position"""
            if t >= duration:
                return -final_offset
            damped_amplitude = amplitude * np.exp(-damping * t)
            return damped_amplitude * np.cos(2 * PI * frequency * t)
        
        def update_spring_and_mass(mob, dt):
            """Update function for spring and mass"""
            current_time = self.renderer.time - start_time
            
            # Get displacement from equilibrium
            displacement = get_position(current_time)
            
            # Update spring length
            new_length = equilibrium_length + displacement
            new_spring = create_spring(new_length, anchor)
            spring.become(new_spring)
            
            # Update mass position
            mass.move_to(spring.get_end())
        
        # Start animation
        start_time = self.renderer.time
        spring.add_updater(update_spring_and_mass)
        
        self.wait(duration + 0.5)
        spring.remove_updater(update_spring_and_mass)
        
        # Final settling animation
        final_spring = create_spring(equilibrium_length + final_offset, anchor)
        final_mass_pos = final_spring.get_end()
        
        self.play(
            Transform(spring, final_spring),
            mass.animate.move_to(final_mass_pos),
            run_time=0.5
        )
        natural_length= DashedLine(eq_line.get_start(),eq_line.get_end(), stroke_width=2, color=ORANGE).next_to(equilibrium_line, UP, buff =0)
        natural_length_label = Text("Natural Length", font_size=24, color=ORANGE).next_to(natural_length, RIGHT, buff=0.2)
        self.play(Create(natural_length), Write(natural_length_label))
        initial_extension = DoubleArrow(start=natural_length.get_start(), end= eq_line.get_start(), color=YELLOW, buff =0)
        intial_extension_label = Text("Initial extension, -x ", font_size=24, color=YELLOW).next_to(initial_extension, LEFT, buff=0.2)
        self.play(Create(initial_extension), Write(intial_extension_label))
        extra_extension = DoubleArrow(start=eq_line.get_start(), end=[eq_line.get_start()[0],mass.get_center()[1],0], color=ORANGE, buff =0)
        extra_extension_label = Text("Extra extension, y ", font_size=24, color=ORANGE).next_to(extra_extension, LEFT, buff=0.2)
        self.play(Create(extra_extension), Write(extra_extension_label))

        spring_weight = LabeledArrow(MathTex(r"mg", font_size=24), start=mass.get_center(), end=mass.get_center()+DOWN*1.5, label_position=0.5)
        spring_force = LabeledArrow(MathTex(r"F = kx", font_size=24), start=mass.get_center(), end=mass.get_center()+UP*1.5, label_position=0.5)
        self.play(Create(spring_weight), Create(spring_force))
        self.wait(2)
        spring_group=VGroup(ceiling, hatches, spring, mass, eq_line, eq_label, natural_length, natural_length_label, initial_extension, intial_extension_label, extra_extension, extra_extension_label, spring_weight, spring_force)
        self.play(spring_group.animate.shift(RIGHT*2))
        Spring_derivation = VGroup(
                MathTex(r"F = kx"), #0
                MathTex(r"mg - kx =0"), #1
                MathTex(r"mg = kx"),#2
                MathTex(r"F = mg - k(x+y)"), #3
                MathTex(r"F = mg- kx - ky"),#4
                MathTex(r"F = -ky"),#5
                MathTex(r"y = - \omega^2 a"), #6
                MathTex(r"a = \frac{F}{m}"),#7
                MathTex(r"y = - \omega^2 \frac{F}{m}"), #8
                MathTex(r"F = - \frac{ym}{\omega^2}"), #9
                MathTex(r"-\frac{ym}{\omega^2}",r"=",r" -ky"), #10
                MathTex(r"\frac{1}{\omega^2}=\frac{m}{k}"), #11
                MathTex(r"\omega = \frac{2\pi}{T}"), #12
                MathTex(r"T = 2\pi \sqrt{\frac{m}{k}}") #13
                ).arrange(DOWN, buff=0.4).to_corner(UL)
        self.play(Write(Spring_derivation[0]))
        self.play(Write(Spring_derivation[1]))
        self.play(Write(Spring_derivation[2]))
        self.play(Write(Spring_derivation[3]))
        self.play(Write(Spring_derivation[4]))
        self.play(Write(Spring_derivation[5]))
        self.wait(2)
        self.play(*[FadeOut(Spring_derivation[n]) for n in range (0,5)], Spring_derivation[5].animate.move_to(Spring_derivation[0])) #tidy up screen
        for n in range (6,14,):   #move the rest up now the other parts have been faded out
            Spring_derivation[n].next_to(Spring_derivation[n-1], DOWN, buff = 0.4)
        self.play(Write(Spring_derivation[6]))
        self.play(Write(Spring_derivation[7]))
        self.play(Write(Spring_derivation[8]))
        self.play(Write(Spring_derivation[9]))
        self.play(*[FadeOut(Spring_derivation[n]) for n in range (6,9)], Spring_derivation[9].animate.next_to(Spring_derivation[5], DOWN, buff =0.4)) #tidy up screen again
        for n in range (10,14):   #move the rest up now the other parts have been faded out
            Spring_derivation[n].next_to(Spring_derivation[n-1], DOWN, buff = 0.35)
        # Animate the pieces of equation 10 from the earlier lines.
        # Create proper MathTex targets for the two parts (not glyph-VMobjects)
        left_target = MathTex(r"-\frac{ym}{\omega^2}", font_size=36)
        right_target = MathTex(r"-ky", font_size=36)
        left_target.move_to(Spring_derivation[10][0].get_center())
        right_target.move_to(Spring_derivation[10][2].get_center())

        # Make copies of the original lines so the originals stay in place
        copy_left = Spring_derivation[5].copy()
        copy_right = Spring_derivation[9].copy()
        self.add(copy_left, copy_right)  # ensure copies are in the scene

        # Animate the copies transforming into the targets and reveal the "="
        self.play(
            TransformMatchingTex(copy_left, left_target),
            TransformMatchingTex(copy_right, right_target),
            FadeIn(Spring_derivation[10][1])
        )

        # Keep the final targets visible as the equation-10 parts (do NOT replace the originals)
        self.add(left_target, right_target)
        # Optionally remove the temporary copies
        self.remove(copy_left, copy_right)

        self.play(Write(Spring_derivation[11]))
        self.play(Write(Spring_derivation[12]))
        self.play(Write(Spring_derivation[13]))
        self.wait(5)
