from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
import numpy as np
# Check for Azure credentials

class Keplers3rdlaw(VoiceoverScene):
    def construct(self):
        # Configure Azure voice service
        azure_service = AzureService(
            voice="en-GB-RyanNeural",
            style="newscast-casual",
        )
        self.set_speech_service(azure_service)
        # Title
        Title = Text("Deriving Kepler's 3rd Law", font_size=48)
        with self.voiceover("In this video we will initially derive Kepler's 3rd law for circular orbits and then adapt it for large planets or binary stars") as tracker:
            self.play(Write(Title))
            # Add underline under the title
            underline = Line(
                Title.get_left(), Title.get_right(), color=WHITE
            ).next_to(Title, DOWN)
            self.play(Create(underline))
            self.wait(2)
        self.play(FadeOut(Title), FadeOut(underline))
        self.wait(2)
        #Recap of Kepler's first two laws
        # Title
        with self.voiceover(text="""First, let's quickly recap Kepler's first two laws of planetary motion. <bookmark mark='title'/>
            """) as tracker:
            title = Text("Kepler's Laws of Planetary Motion", font_size=40)
            title.to_edge(UP)
            self.play(Write(title))
            self.wait_until_bookmark("title")
            self.wait(2)
            # First Law
        with self.voiceover(text="""Kepler's 1st law states that planets move in elliptical orbits with the Sun at one focus. <bookmark mark='first_law'/>
            """) as tracker:
            law1_text = Text("1st Law: Law of Ellipses", font_size=32, color=BLUE)
            law1_text.next_to(title, DOWN, buff=0.5)
            
            law1_desc = Text(
                "Planets move in elliptical orbits with the Sun at one focus",
                font_size=24
            )
            law1_desc.next_to(law1_text, DOWN, buff=0.3)
            
            self.play(Write(law1_text))
            self.play(Write(law1_desc))
            
            # Draw ellipse diagram
            ellipse = Ellipse(width=4, height=2.5, color=WHITE)
            ellipse.shift(DOWN * 1)
            
            # Calculate foci positions (for ellipse: c = sqrt(a^2 - b^2))
            a = 2  # semi-major axis
            b = 1.25  # semi-minor axis
            c = np.sqrt(a**2 - b**2)
            
            # Foci positions
            focus1_pos = ellipse.get_center() + LEFT * c
            focus2_pos = ellipse.get_center() + RIGHT * c
            
            # Draw the ellipse
            self.play(Create(ellipse))
            
            # Mark the foci
            focus1 = Dot(focus1_pos, color=RED)
            focus2 = Dot(focus2_pos, color=YELLOW, radius=0.15)
            
            self.play(FadeIn(focus1), FadeIn(focus2))
            
            # Label the Sun
            sun_label = Text("Sun", font_size=20, color=YELLOW)
            sun_label.next_to(focus2, DOWN, buff=0.2)
            self.play(Write(sun_label))
            
            # Optional: Show empty focus label
            empty_focus_label = Text("Empty Focus", font_size=18, color=RED)
            empty_focus_label.next_to(focus1, DOWN, buff=0.2)
            self.play(Write(empty_focus_label))
            self.wait(2)
            # Clear for second law
            self.play(
                FadeOut(ellipse),
                FadeOut(focus1),
                FadeOut(focus2),
                FadeOut(sun_label),
                FadeOut(empty_focus_label),
                FadeOut(law1_text),
                FadeOut(law1_desc)
            )
            self.wait_until_bookmark("first_law")
            self.wait(3)
        with self.voiceover(text="""Kepler's 2nd law states that a line joining a planet and the Sun sweeps out equal areas in equal times. 
                This means any planet orbiting a star must travel faster when closer to the star and slower as it moves further away. <bookmark mark='second_law'/>
            """) as tracker:
            # Second Law
            law2_text = Text("2nd Law: Law of Equal Areas", font_size=32, color=GREEN)
            law2_text.next_to(title, DOWN, buff=0.5)
            
            law2_desc = Text(
                "A line joining a planet and the Sun sweeps out\nequal areas in equal times",
                font_size=24
            )
            law2_desc.next_to(law2_text, DOWN, buff=0.3)
            
            self.play(Write(law2_text))
            self.play(Write(law2_desc))
            self.wait()
            
            # Draw ellipse for second law
            ellipse2 = Ellipse(width=4, height=2.5, color=WHITE)
            ellipse2.shift(DOWN * 1.2)
            
            # Sun position at left focus
            sun_pos = ellipse2.get_center() + LEFT * c
            sun2 = Dot(sun_pos, color=YELLOW, radius=0.15)
            sun2_label = Text("Sun", font_size=18, color=YELLOW)
            sun2_label.next_to(sun2, DOWN, buff=0.15)
            
            self.play(Create(ellipse2), FadeIn(sun2), Write(sun2_label))
            self.wait()
            
            # Create planet
            planet = Dot(ellipse2.point_at_angle(0), color=BLUE, radius=0.1)
            self.play(FadeIn(planet))
            
            # First sweep: near perihelion (fast, small arc)
            angle1_start = 0
            angle1_end = 0.8
            duration1 = 2
            
            # Create traced area that updates with planet
            area1_trace = always_redraw(lambda: Polygon(
                sun_pos,
                *[ellipse2.point_at_angle(angle1_start + (angle1_end - angle1_start) * i / 30) 
                for i in range(31)],
                color=BLUE,
                fill_opacity=0,
                stroke_width=0
            ))
            
            # Use ValueTracker to control the animation
            tracker1 = ValueTracker(0)
            
            def get_area1():
                alpha = tracker1.get_value()
                if alpha < 0.01:
                    return Polygon(sun_pos, ellipse2.point_at_angle(angle1_start), sun_pos,
                                fill_opacity=0, stroke_width=0)
                current_angle = angle1_start + (angle1_end - angle1_start) * alpha
                points = [sun_pos]
                steps = max(3, int(30 * alpha))
                for i in range(steps + 1):
                    angle = angle1_start + (angle1_end - angle1_start) * i / steps
                    points.append(ellipse2.point_at_angle(angle))
                points.append(sun_pos)
                return Polygon(*points, color=BLUE, fill_opacity=0.3, stroke_width=2)
            
            area1_mob = always_redraw(get_area1)
            self.add(area1_mob)
            
            # Animate planet and area together
            self.play(
                UpdateFromFunc(planet, lambda m: m.move_to(
                    ellipse2.point_at_angle(angle1_start + (angle1_end - angle1_start) * tracker1.get_value())
                )),
                tracker1.animate.set_value(1),
                run_time=duration1,
                rate_func=linear
            )
            
            area1_label = Text("Area 1", font_size=20, color=BLUE)
            area1_label.next_to(ellipse2.point_at_angle(0.4), DOWN, buff=0.3)
            self.play(Write(area1_label))
            self.wait()
            
            # Second sweep: near aphelion (slow, large arc)
            angle2_start = PI - 0.7
            angle2_end = PI + 0.7
            duration2 = 2  # Same duration, but larger arc
            
            # Move planet to start of second sweep
            self.play(planet.animate.move_to(ellipse2.point_at_angle(angle2_start)), run_time=1)
            
            tracker2 = ValueTracker(0)
            
            def get_area2():
                alpha = tracker2.get_value()
                if alpha < 0.01:
                    return Polygon(sun_pos, ellipse2.point_at_angle(angle2_start), sun_pos,
                                fill_opacity=0, stroke_width=0)
                current_angle = angle2_start + (angle2_end - angle2_start) * alpha
                points = [sun_pos]
                steps = max(3, int(30 * alpha))
                for i in range(steps + 1):
                    angle = angle2_start + (angle2_end - angle2_start) * i / steps
                    points.append(ellipse2.point_at_angle(angle))
                points.append(sun_pos)
                return Polygon(*points, color=RED, fill_opacity=0.3, stroke_width=2)
            
            area2_mob = always_redraw(get_area2)
            self.add(area2_mob)
            
            self.play(
                UpdateFromFunc(planet, lambda m: m.move_to(
                    ellipse2.point_at_angle(angle2_start + (angle2_end - angle2_start) * tracker2.get_value())
                )),
                tracker2.animate.set_value(1),
                run_time=duration2,
                rate_func=linear
            )
            
            area2_label = Text("Area 2", font_size=20, color=RED)
            area2_label.next_to(ellipse2.point_at_angle(PI), LEFT, buff=0.3)
            self.play(Write(area2_label))
            
            # Add note about equal areas
            equal_note = Text("Both areas swept in equal time!", font_size=18, color=YELLOW)
            equal_note.to_edge(DOWN, buff=0.3)
            self.play(Write(equal_note))
            self.wait_until_bookmark("second_law")
            self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        # Derivation
        thirdlaw_title = Text("Deriving Kepler's 3rd Law", font_size=48).to_edge(UP)
        centripetal_force = MathTex(r"F", r"=",r" m \omega^2 r")
        gravitation= MathTex(r"F", r"=",r"\frac {GMm}{r^2}").next_to(centripetal_force, DOWN)
        substituted = MathTex(r"m \omega^2 r", "=", r"\frac {GMm}{r^2}").next_to(centripetal_force, DOWN)
        omega_def = MathTex (r"\omega", r"=\frac{2\pi}{T}").next_to(centripetal_force, DOWN, buff=0.5)
        omega_squared = MathTex (r"\omega^2", r"=\frac{4\pi^2}{T^2}").next_to(centripetal_force, DOWN, buff=0.5)
        substitution = MathTex(r" m\frac{4\pi^2}{T^2} r", "=", r"\frac {GMm}{r^2}")
        group_terms = MathTex(r"\frac {GMm}{m r^3}",r"=\frac{4\pi^2}{T^2}" ).next_to(substitution, DOWN, buff=0.5)
        final = MathTex (r"T^2","=", r"\frac{4\pi^2}{GM} r^3").next_to(group_terms, DOWN, buff=0.5)
        thirdlawtext1 = Text("Law 3: Law of proportions", font_size=36, color= RED).next_to(thirdlaw_title, DOWN, buff=1)
        thirdlawtext2 = Text("The square of the orbital period is proportional to the cube of the semi-major axis of the orbit.", font_size=20).next_to(thirdlawtext1, DOWN, buff=0.3)
        thirdlawtext = VGroup(thirdlawtext1, thirdlawtext2)
        #step through derivation
        with self.voiceover(text="""Now to derive Kepler's 3rd law for circular orbits,<bookmark mark='titleover'/>
            At first we will simplfy our model for planets by assuming that they move in circular orbits. 
            We will start by considering the forces acting on our planet. We have the centripetal force that causes our planet to move in a circle. <bookmark mark='centripetal'/>                
            This force is provided by the gravitational attraction between the planet and the sun, which we can express using Newton's law of gravitation. <bookmark mark='gravitation'/>
            As these two forces are equal, we can set them equal to each other. <bookmark mark='equal'/>
            Omega is the angular velocity, which we can define in terms of the orbital period T.<bookmark mark='omega'/>
            We will then square, <bookmark mark='square'/> and substitute this into our equation. <bookmark mark='substitute'/>
            Next, we can group our terms to isolate T^2 on one side of the equation. <bookmark mark='group'/>
            Finally, we can rearrange to get Kepler's 3rd law, which states that the square of the orbital period is proportional to the cube of the semi-major axis of the orbit. <bookmark mark='final'/>
            """) as tracker:
            self.play(Write(thirdlaw_title))
            self.wait_until_bookmark("titleover")
            self.play(Write(centripetal_force))
            self.wait_until_bookmark("centripetal")
            self.play(Write(gravitation))
            substituted.move_to(gravitation)
            self.wait_until_bookmark("gravitation")
    # Transform F in gravitation to the expression from centripetal force
    # Transform the F in gravitation to the expression from centripetal force
            self.play(
                TransformFromCopy(centripetal_force[2], substituted[0]),
                ReplacementTransform(gravitation[1], substituted[1]),
            ReplacementTransform(gravitation[2], substituted[2]),
                FadeOut(gravitation[0]),
                FadeOut(centripetal_force),
                substituted.animate.move_to(ORIGIN)
        )
            self.wait_until_bookmark("equal")
            self.play(Write(omega_def))
            self.wait_until_bookmark("omega")
            self.play(ReplacementTransform(omega_def, omega_squared))
            self.wait_until_bookmark("square")
            self.play(
   
                TransformFromCopy(omega_squared[1], substitution[0]),
                ReplacementTransform(substituted[0], substitution[1]),
                ReplacementTransform(substituted[1], substitution[1]),
                FadeOut(substituted[1]),
                FadeOut(substituted[2]),  
                Write(substitution[1]),
                Write(substitution[2]),    
                FadeOut(omega_squared),
                substitution.animate.move_to(ORIGIN)
            )
            self.wait_until_bookmark("substitute")
            self.play(Write(group_terms))
            self.wait_until_bookmark("group")
            self.play(Write(final))
            self.play(Write(thirdlawtext))
            self.wait_until_bookmark("final")
            self.play(*[FadeOut(mob) for mob in self.mobjects],
                      FadeOut(substitution[0]),FadeOut(substitution[2])
            )
            self.wait(2)
        epltical_title = Text("Extending to Large Planets", font_size=48).to_edge(UP)
        moments = MathTex(r"m_1 r_1", r"=", r"m_2 r_2").next_to(epltical_title, DOWN, buff=1.2)
        distance_between = MathTex(r"r_1", r"+", r"r_2", r"=", r"d").next_to(moments, DOWN, buff=0.4)
        moments_derivation1 = MathTex(r"r_1", r"=", r"d-r_2").next_to(moments, DOWN, buff=0.4)
        moments_derivation2 = MathTex(r"m_1 (d-r_2)", r"=", r"m_2 r_2").next_to(epltical_title, DOWN, buff=1)

        
        with self.voiceover(text="""The previous derivation assumed circular orbits, which for the moost part is a reasonable approximation for many planets, where their mass is very small compared to the star, so the centre of mass of the system is within the star. <bookmark mark='title'/>
            However, for very large planets or binary star systems, the centre of mass can lie outside of either body, this means that in our original derivation, the distance for gravitation and for centripetal force are now longer the same.
            Gravitation relies on the distance between the two objects, whereas centripetal force relies on the distance from each object to the centre of mass.
            Lets first visualise this and define some terms. Here we have our large planet and its star, the distance between them is d, and the distance for each object from the centre of mass is r1 for the Star and r2 for the planet. <bookmark mark ='diagram'/>
            As these two objects orbit their common centre of mass, they are in equilibrium, so there is no net moment and no net force on the system. 
            This means that the moment both both objects create on the centre of mass must be equal. From this we can derive that m1 r1 = m2 r2, and from this we can also derive that r1 + r2 = d. <bookmark mark='mom'/>
            From this we can substitute r1 and r2 in terms of d, giving us r1 = (m2 / (m1 + m2)) d and r2 = (m1 / (m1 + m2)) d. <bookmark mark='definitions'/>
            Now we can adapt our derivation of Kepler's 3rd law to account for this. 
            """) as tracker:
            self.play(Write(epltical_title))
            #Draw two large bodies orbiting their common centre of mass
            planet1 = Dot(np.array([-2,0,0]), color=YELLOW, radius=0.4)
            planet2 = Dot(np.array([2,0,0]), color=RED, radius=0.2)
            x= (2*0.2)/(0.4+0.2)  #Distance of centre of mass from larger planet
            point = np.array([x-2, 0, 0]) #Needs to have the x offset to position relative to larger planet
            com = Cross(stroke_color=ORANGE, scale_factor=0.2).move_to(point) #Centre of mass position
            d = DoubleArrow(
            start=planet1.get_center(),
            end=planet2.get_center(),
            color=RED,
            # Use tip_shape_start and tip_shape_end to define the bar ends
            tip_shape_start=StealthTip,
            tip_shape_end=StealthTip,
            tip_length=0.25
            )
        
        # You can still use .move_to() if you want to reposition the whole line
            d.move_to(UP * 0.5)
            d_label = MathTex("d", color=ORANGE, font_size=24)
            d_label.next_to(d, UP, buff=0.1)
            r1= DoubleArrow(np.array([x-2, 0, 0]), planet1.get_center(), color=PURE_GREEN,tip_shape_start=StealthTip, tip_shape_end=StealthTip, tip_length=1)
            r1_label = MathTex("r_1", color=PURE_GREEN, font_size=24)
            r1_label.next_to(r1, DOWN, buff=0.4)
            r2= DoubleArrow(com.get_center(), planet2.get_center(), color=PURE_GREEN, tip_shape_start=StealthTip, tip_shape_end=StealthTip, tip_length=0.25)
            r2_label = MathTex("r_2", color=PURE_GREEN, font_size=24)
            r2_label.next_to(r2, DOWN, buff=0.2)
        
            self.play(FadeIn(planet1, planet2, com),
                      Create(d), Write(d_label),
                      Create(r1), Write(r1_label),
                        Create(r2), Write(r2_label))
            com_label = Text("Center of Mass", font_size=18, color=YELLOW).next_to(com, DOWN, buff=0.5)
            self.play(Write(com_label))
            largeplanets= VGroup(planet1, planet2, com, d, d_label, r1, r1_label, r2, r2_label, com_label)
            self.play(Rotate(largeplanets, angle=2*PI, about_point=com.get_center(), run_time=10, rate_func=linear))
            self.wait_until_bookmark("diagram")
            self.play(FadeOut(epltical_title))
            self.play(largeplanets.animate.to_edge(UP))
            moments.next_to(largeplanets, DOWN, buff = 0.5)
            moments_derivation2.next_to(largeplanets, DOWN, buff = 0.5)
            self.play(Write(moments))
            self.wait(2)
            self.play(Write(distance_between))
            self.wait(2)
            self.play(Transform(distance_between, moments_derivation1))
            self.wait_until_bookmark("mom")
            self.play(Transform(moments, moments_derivation2), FadeOut(distance_between))
            moments_derivation3 = MathTex(r"m_1 d - m_1 r_2", r"=", r"m_2 r_2").next_to(moments_derivation2, DOWN, buff=0.4)
            moments_derivation4 = MathTex(r"m_1 d", r"=", r"m_1 r_2 + m_2 r_2").next_to(moments_derivation3, DOWN, buff=0.4)
            moments_derivation5 = MathTex(r"m_1 d", r"=", r"(m_1 + m_2) r_2").next_to(moments_derivation4, DOWN, buff=0.4)
            r2_definition = MathTex(r"r_2", r"=", r"\frac{m_1}{m_1 + m_2} d").next_to(moments_derivation5, DOWN, buff=0.4)
            r1_definition = MathTex(r"r_1", r"=", r"\frac{m_2}{m_1 + m_2} d").next_to(r2_definition, DOWN, buff=0.4)
            r1r2group = VGroup(r2_definition,r1_definition).arrange(RIGHT, buff=1).next_to(moments_derivation5, DOWN, buff = 0.4)
            self.wait(2)
            self.play(Write(moments_derivation3))
            self.wait(2)
            self.play(Write(moments_derivation4))
            self.wait(2)
            self.play(Write(moments_derivation5))
            self.wait(2)
            self.play(Write(r1r2group))
            self.wait_until_bookmark ("definitions")
            self.play(*[FadeOut(mob) for mob in self.mobjects])
            gravitation_binary = MathTex(r"F",r"=",r"\frac {G m_1 m_2}{d^2}" ).to_edge(UP, buff = 0.25)
            centripetal_binary = MathTex(r"F",r"=",r"M_1 \omega ^2 r_1").next_to(gravitation_binary, DOWN, buff = 0.4)
            centripetal_binary_r1_sub = MathTex (r"F",r"=",r"m_1 \omega ^2 \frac{m_2}{m_1 + m_2} d").next_to(gravitation_binary, DOWN, buff = 0.4)
            equations_equal = MathTex (r"m_1 \omega ^2 \frac{m_2}{m_1 + m_2} d",r"=",r"\frac {G m_1 m_2}{d^2}" ).next_to(centripetal_binary_r1_sub, DOWN, buff = 0.6)
            equations_omega_sub = MathTex(r"\frac{(m_1 + m_2) 4 \pi ^2 d} {t^2}",r"=",r"\frac {G}{d^2}" ).next_to(centripetal_binary_r1_sub, DOWN, buff = 0.6)
            final_equation = MathTex(r"t^2",r"=",r"\frac{4 \pi^2 d^3}{G(m_1 + m_2)}").next_to(equations_omega_sub, DOWN, buff = 0.4)
            final_equation_largemass = MathTex(r"t^2",r"=",r"\frac{4 \pi^2 d^3}{G M_1}").next_to(final_equation, DOWN, buff = 0.4)
        with self.voiceover (text ="""
            Now we have our formula relating the distance between the objects, required for gravitation and the distance from the centre of rotation, required for centripetal force. We can add these to our formulas and rederive Kepler's 3rd law.
            So now our formula for centripetal acceleration becomes m 1 omega squared r 1 and our law of gravitation becomes G M 1 M 2 over d squared.<bookmark mark ='formula'/>
            First, lets remove r 1 from the equation by subsituting our previous equation for r1. <bookmark mark="subin"/>
            Next equate these two equations to each other <bookmark mark='equate'/>
            As we have an m 1 m2 term on both sides, these cancel <bookmark mark='cancel'/>
            We subsitute our definition for omega squared in again <bookmark mark='omega'/>
            And finally we rearrange to get T squared as the subject. <bookmark mark='simplify'/>
            For a system where m1 is very much larger than m2, then m1 + m2 approximately equals m1. So this simplifies back to this verison of keplers law back to our previous version
        """)as tracker:
            self.play(Write(gravitation_binary),
                      Write(centripetal_binary))
            self.wait_until_bookmark ("formula")
            self.play(Transform(centripetal_binary,centripetal_binary_r1_sub))
            self.wait_until_bookmark ("subin")
            self.play(Write(equations_equal))
            self.wait_until_bookmark("equate")
            self.play(Transform(equations_equal,equations_omega_sub))
            self.wait_until_bookmark ("omega")
            self.play(Write(final_equation))
            self.wait_until_bookmark("simplify")
            self.play(Write(final_equation_largemass))
            self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        with self.voiceover(text="""In summary, Kepler's 3 laws are as follows.
                1) Planets orbit their parent star in elipses with the star at one of the foci of the elipse <bookmark mark='1stlaw'/>
                2) A line between the planet and the parent star will sweep our equal areas in equal time <bookmark mark='2ndlaw'/>
                3) The square of the time period is proportional to the mean orbital radius cubed. <bookmark mark='3rdlaw'/>
                We have shown that in this video the thrid law also holds for binary stars where the centre of orbit is not within the larger body.
                Hopefully this video has helped and if you have any questions post them below, like and subscribe!
            """) as tracker:
            Summary = Text("In Summary", font_size=48).to_edge(UP)
            self.play (Write(Summary))
            law1_text.next_to(Summary, DOWN, buff=0.5)
            law1_desc.next_to(law1_text, DOWN, buff=0.3)
            self.play(Write(law1_text), Write(law1_desc))
            self.wait_until_bookmark ("1stlaw")
            law2_text.next_to(law1_desc, DOWN, buff=0.5)
            law2_desc.next_to(law2_text, DOWN, buff=0.3)
            self.play(Write(law2_text), Write(law2_desc))
            self.wait_until_bookmark ("2ndlaw")
            thirdlawtext.next_to(law2_desc,DOWN,buff =0.5)
            self.play(Write(thirdlawtext))
            self.wait_until_bookmark("3rdlaw")
        self.play(*[FadeOut(mob) for mob in self.mobjects])