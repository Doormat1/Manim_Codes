from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class Escape(VoiceoverScene):
    def construct(self):
        # Configure Azure voice service
        azure_service = AzureService(
            voice="en-GB-RyanNeural",
            style="newscast-casual",
        )
        self.set_speech_service(azure_service)
        Title = Text("Deriving Escape Velocities from E and G Fields", font_size=48).to_edge(UP)
        with self.voiceover("In this video, we will use the definition of the potential of a field to calculate the escape velocity for electric and gravitational fields") as tracker:
            self.play(Write(Title))
            # Add underline under the title
            underline = Line(
                Title.get_left(), Title.get_right(), color=WHITE
            ).next_to(Title, DOWN)
            self.play(Create(underline))
            self.wait(2)
        self.play(FadeOut(Title), FadeOut(underline))
        self.wait(1)
        # Escape velocity from an electric field
        EV = MathTex(r"V_e = \frac{1}{4\pi\epsilon_0}\frac{Q}{R^2}", font_size=48).to_edge(UP)
        wd = MathTex(r"Work Done = Q\Delta V ", font_size = 48).next_to (EV,DOWN)
        delta_EV = MathTex(r"\Delta V = \frac{1}{4\pi\epsilon_0}(\frac{Q}{R_2}-\frac{Q}{R_1})", font_size=48).next_to(wd, DOWN)
        delta_EV2 = MathTex(r"\Delta V = \frac{1}{4\pi\epsilon_0}(\frac{Q}{\infty}-\frac{Q}{R})", font_size=48).next_to(delta_EV, DOWN)
        delta_EV3 = MathTex(r"\Delta V = \frac{1}{4\pi\epsilon_0}\frac{Q}{R}", font_size=48).next_to(delta_EV2, DOWN)
        ke = MathTex(r"KE = \frac{1}{2}mv^2", font_size=48).next_to(delta_EV3, DOWN)
        eq = MathTex(r"\frac{1}{2}mv^2 = Q\Delta V", font_size=48).next_to(ke, DOWN)
        eq2 = MathTex(r"\frac{1}{2}mv^2 = Q(\frac{1}{4\pi\epsilon_0}\frac{Q}{R})", font_size=48).next_to(eq, DOWN)    
        EV_final = MathTex(r"v_e = \sqrt{\frac{1}{2\pi\epsilon_0}\frac{Q^2}{mR}}", font_size=48).next_to(eq2, DOWN)
        equations = VGroup()
         # Arrange all equations vertically with some spacing
        with self.voiceover(text="""First, let's consider an electric field created by a point charge. The electric potential at a distance R from the charge is given by this equation. <bookmark mark='electricpotential'/> 
            In order to escape the field, we need to calculate how much work is done in moving a particle through this change in electric potential, this is equal to the change in potential times the charge.
            To escape the electric field, a particle must be moved from a distance R to infinity, where the potential is zero. Therefore, we can calculate the change in electric potential as follows. <bookmark mark='changepotential'/>
            Next, we substitute R2 with infinity and R1 with R in the change in potential equation. <bookmark mark='substitution'/> 
            Since the potential at infinity is zero, we can simplify the equation to get this expression for the change in electric potential. <bookmark mark='simplification'/> 
            The kinetic energy of a particle with mass m and velocity v is given by this equation. <bookmark mark='kineticenergy'/> 
            To find the escape velocity, we set the kinetic energy equal to the work done in moving the particle through the change in electric potential. <bookmark mark='workdone'/> 
            Substituting our expression for change in electric potential into this equation gives us this equation. <bookmark mark='substitution2'/> 
            Finally, we rearrange the equation to solve for v, giving us our final expression for the escape velocity from an electric field. <bookmark mark='finalelectric'/>""") as tracker:
           # Add first equation
            equations.add(EV)
            EV.to_edge(UP)
            self.play(Write(EV))
            self.wait_until_bookmark("electricpotential")
            
            # Function to add new equation
            def add_equation(new_eq):
                    new_eq.next_to(equations[-1], DOWN, buff=0.3)
                    # Check if the new equation goes off screen
                    if new_eq.get_bottom()[1] < -3.5:
                        shift_amount = abs(new_eq.get_bottom()[1] + 3.5)
                        # Shift existing equations up first
                        self.play(equations.animate.shift(UP * shift_amount))
                        new_eq.next_to(equations[-1], DOWN, buff=0.3)
                        # Then write the new equation at its original position
                        self.play(Write(new_eq))
                    else:
                        self.play(Write(new_eq))
                    equations.add(new_eq)
        
            add_equation(wd)
            self.wait_until_bookmark("changepotential")
            add_equation(delta_EV)
            self.wait_until_bookmark("substitution")
            add_equation(delta_EV2)
            self.wait_until_bookmark("simplification")
            add_equation(delta_EV3)
            self.wait_until_bookmark("kineticenergy")
            add_equation(ke)
            self.wait_until_bookmark("workdone")
            add_equation(eq)
            self.wait_until_bookmark("substitution2")
            add_equation(eq2)
            self.wait_until_bookmark("finalelectric")
            add_equation(EV_final)
            self.wait(5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
        # Escape velocity from a gravitational field
        GV = MathTex(r"V = -\frac{GM}{R}", font_size=48).to_edge(UP)
        wd2 = MathTex(r"Work Done = m \Delta V ", font_size = 48).next_to (GV,DOWN)
        delta_GV = MathTex(r"\Delta V = GM(\frac{1}{R_2}-\frac{1}{R_1})", font_size=48).next_to(wd2, DOWN)
        delta_GV2 = MathTex(r"\Delta V = GM(\frac{1}{\infty}-\frac{1}{R})", font_size=48).next_to(delta_GV, DOWN)
        delta_GV3 = MathTex(r"\Delta V = \frac{GM}{R}", font_size=48).next_to(delta_GV2, DOWN)
        ke2 = MathTex(r"KE = \frac{1}{2}mv^2", font_size=48).next_to(delta_GV3, DOWN)
        eq3 = MathTex(r"\frac{1}{2}mv^2 = m\Delta V", font_size=48).next_to(ke2, DOWN)
        eq4 = MathTex(r"\frac{1}{2}mv^2 = m(GM(\frac{1}{R}))", font_size=48).next_to(eq3, DOWN)
        GV_final = MathTex(r"v_e = \sqrt{\frac{2GM}{R}}", font_size=48).next_to(eq4, DOWN)
        equations2 = VGroup()
         # Arrange all equations vertically with some spacing

        with self.voiceover(text="""Now, let's consider a gravitational field created by a mass M. The gravitational potential at a distance R from the mass is given by this equation. <bookmark mark='gravitationalpotential'/>
            In order to escape the field, we need to calculate how much work is done in moving a particle through this change in gravitational potential, this is equal to the change in potential times the mass.
            To escape the gravitational field, a particle must be moved from a distance R to infinity, where the potential is zero. Therefore, we can calculate the change in gravitational potential as follows. <bookmark mark='changepotentialg'/>
            Next, we substitute R2 with infinity and R1 with R in the change in potential equation. <bookmark mark='substitutiong'/> 
            Since the potential at infinity is zero, we can simplify the equation to get this expression for the change in gravitational potential. <bookmark mark='simplificationg'/> 
            The kinetic energy of a particle with mass m and velocity v is given by this equation. <bookmark mark='kineticenergyg'/> 
            To find the escape velocity, we set the kinetic energy equal to the work done in moving the particle through the change in gravitational potential. <bookmark mark='workdoneg'/> 
            Substituting our expression for change in gravitational potential into this equation gives us this equation. <bookmark mark='substitution2g'/> 
            Finally, we rearrange the equation to solve for v, giving us our final expression for the escape velocity from a gravitational field. <bookmark mark='finalgravitational'/>""") as tracker:
           # Add first equation
            equations2.add(GV)
            GV.to_edge(UP)
            self.play(Write(GV))
            self.wait_until_bookmark("gravitationalpotential")
            
            # Function to add new equation
            def add_equation2(new_eq):
                    new_eq.next_to(equations2[-1], DOWN, buff=0.3)
                    # Check if the new equation goes off screen
                    if new_eq.get_bottom()[1] < -3.5:
                        shift_amount = abs(new_eq.get_bottom()[1] + 3.5)
                        # Shift existing equations up first
                        self.play(equations2.animate.shift(UP * shift_amount))
                        new_eq.next_to(equations2[-1], DOWN, buff=0.3)
                        # Then write the new equation at its original position
                        self.play(Write(new_eq))
                    else:
                        self.play(Write(new_eq))
                    equations2.add(new_eq)
            add_equation2(wd2)
            self.wait_until_bookmark("changepotentialg")
            add_equation2(delta_GV)
            self.wait_until_bookmark("substitutiong")
            add_equation2(delta_GV2)
            self.wait_until_bookmark("simplificationg")
            add_equation2(delta_GV3)
            self.wait_until_bookmark("kineticenergyg")
            add_equation2(ke2)
            self.wait_until_bookmark("workdoneg")
            add_equation2(eq3)
            self.wait_until_bookmark("substitution2g")
            add_equation2(eq4)
            self.wait_until_bookmark("finalgravitational")
            add_equation2(GV_final)
            self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
        # Summary
        with self.voiceover(text="To summarise, we found the escape velocity from an electric field is equal to the square root of 1 over 2 pi epsilon naught times Q squared over m R and the escape velocity from a gravitational field is the square root of 2GM over R. Hope this video helps and thanks for watching!") as tracker:
            EV_final.move_to(ORIGIN)  # Centers the equation
            self.play(Write(EV_final))
            GV_final2 = MathTex(r"v_e = \sqrt{\frac{2GM}{R}}", font_size=48).next_to(EV_final, DOWN)
            GV_final2.next_to(EV_final, DOWN)
            self.play(Write(GV_final2))
            self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

