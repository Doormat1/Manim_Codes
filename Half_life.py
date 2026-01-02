from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class HalfLife(VoiceoverScene):
    def construct(self):
        # Configure Azure voice service
        azure_service = AzureService(
            voice="en-GB-RyanNeural",
            style="newscast-casual",
        )
        self.set_speech_service(azure_service)
        # Title
        Title = Text("Half Life for Exponetial Decay", font_size=48)
        with self.voiceover("In this video, we will derive expressions for the half life of a radioisotope in terms of its decay equation and for a capacitor, resistor series combination in terms of their time constant") as tracker:
            self.play(Write(Title))
            # Add underline under the title
            underline = Line(
                Title.get_left(), Title.get_right(), color=WHITE
            ).next_to(Title, DOWN)
            self.play(Create(underline))
            self.wait(2)
        self.play(FadeOut(Title), FadeOut(underline))
        # Radioisotope half life
        Radioisotope = Text("Radioisotope Half Life", font_size=36)
        decay_constant = MathTex(r"\lambda", font_size=36)
        decay_eq = MathTex(r"N(t) = N_0 e^{-\lambda t}", font_size=36)
        half_life_eq = MathTex(r"N(t_{1/2}) = \frac{N_0}{2}", font_size=36)
        half_life_eq_sub = MathTex(r"\frac{N_0}{2} = N_0 e^{-\lambda t_{1/2}}", font_size=36)
        half_life_eq_sub_div = MathTex(r"\frac{1}{2} = e^{-\lambda t_{1/2}}", font_size=36)
        half_life_eq_sub_ln = MathTex(r"\ln\left(\frac{1}{2}\right) = -\lambda t_{1/2}", font_size=36)
        half_life_eq_final = MathTex(r"t_{1/2} = \frac{\ln(2)}{\lambda}", font_size=36)

        with self.voiceover(text="""First, let's consider a radioisotope that decays over time. 
            The decay constant, lambda is can be thought of the chance of an atom decaying per second. <bookmark mark='decayconstant'/> 
            All radioisotopes exhibit exponential decay and follow this decay equation <bookmark mark='exponetialdecay'/> 
            The half life of a radioisotope is defined as the time it takes for half of the atoms to decay. Therefore, we can set N(t) equal to half of the initial amount of atoms, N0 <bookmark mark='halflife'/> 
            Next we substitute t with t 1/2 and N(t) with N0/2 in the decay equation. <bookmark mark='sub'/> 
            To solve for t 1/2, we first divide both sides by N0 <bookmark mark='div'/>  and then take the natural log of both sides. <bookmark mark='ln'/> 
            Next, we use log laws to remove the minus sign from the exponent by flipping the fraction.
            Finally, we rearrange the equation to get our final expression for the half life of a radioisotope in terms of its decay constant. <bookmark mark='final'/>
            """) as tracker:
            self.play(Write(Radioisotope))
            self.wait(1)
            self.play(Transform(Radioisotope, decay_constant))
            self.wait_until_bookmark("decayconstant")
            self.play(Transform(Radioisotope, decay_eq))
            self.wait_until_bookmark("exponetialdecay")
            self.play(Transform(Radioisotope, half_life_eq))
            self.wait_until_bookmark("halflife")
            self.play(Transform(Radioisotope, half_life_eq_sub))
            self.wait_until_bookmark("sub")
            self.play(Transform(Radioisotope, half_life_eq_sub_div))
            self.wait_until_bookmark("div")
            self.play(Transform(Radioisotope, half_life_eq_sub_ln))
            self.wait_until_bookmark("ln")
            self.play(Transform(Radioisotope, half_life_eq_final))
            self.wait_until_bookmark("final")
            self.wait(2)
        self.play(FadeOut(Radioisotope))
        # RC Circuit half life
        RC = Text("RC Circuit Half Life", font_size=36)
        time_constant = MathTex(r"\tau = RC", font_size=36)
        rc_eq = MathTex(r"Q(t) = Q_0 e^{-\frac{t}{RC}}", font_size=36)
        rc_half_life_eq = MathTex(r"Q(t_{1/2}) = \frac{Q_0}{2}", font_size=36)
        rc_half_life_eq_sub = MathTex(r"\frac{Q_0}{2} = Q_0 e^{-\frac{t_{1/2}}{RC}}", font_size=36)
        rc_half_life_eq_sub_div = MathTex(r"\frac{1}{2} = e^{-\frac{t_{1/2}}{RC}}", font_size=36)
        rc_half_life_eq_sub_ln = MathTex(r"\ln\left(\frac{1}{2}\right) = -\frac{t_{1/2}}{RC}", font_size=36)
        rc_half_life_eq_final = MathTex(r"t_{1/2} = RC \ln(2)", font_size=36)  
        rc_half_life_eq_final2 = MathTex(r"t_{1/2} = \tau \ln(2)", font_size=36)
        with self.voiceover(text="""Now lets consider a capacitor discharging through a resistor.
            Firstly, we define the time constant, tau, as resistance, R, times capacitance, C.  <bookmark mark='decayconstant'/> 
            For a capacitor discharging through a resistor, the charge, Q at time t, is given by Q = Q naught, e to the power of minus t over RC. <bookmark mark='exponetialdecay'/> 
            The half life of a radioisotope is defined as the time it takes for the charge of our capacitor to drop to half the initial charge. <bookmark mark='halflife'/> 
            Next we substitute t with t 1/2 and Q(t) with Q0/2 in the decay equation. <bookmark mark='sub'/> 
            To solve for t 1/2, we first divide both sides by Q0 <bookmark mark='div'/>  and then take the natural log of both sides. <bookmark mark='ln'/> 
            Finally, we rearrange the equation to get our final expression for the half life of a radioisotope in terms of its decay constant. <bookmark mark='final'/>
            We can also express this in terms of the time constant, tau. <bookmark mark='final2'/>
            """) as tracker:
            self.play(Write(RC))
            self.wait(1)
            self.play(Transform(RC, time_constant))
            self.wait_until_bookmark("decayconstant")
            self.play(Transform(RC, rc_eq))
            self.wait_until_bookmark("exponetialdecay")
            self.play(Transform(RC, rc_half_life_eq))
            self.wait_until_bookmark("halflife")
            self.play(Transform(RC, rc_half_life_eq_sub))       
            self.wait_until_bookmark("sub")
            self.play(Transform(RC, rc_half_life_eq_sub_div))           
            self.wait_until_bookmark("div")
            self.play(Transform(RC, rc_half_life_eq_sub_ln))    
            self.wait_until_bookmark("ln")
            self.play(Transform(RC, rc_half_life_eq_final)) 
            self.wait_until_bookmark("final")
            self.play(Transform(RC, rc_half_life_eq_final2))    
            self.wait_until_bookmark("final2")
            self.wait(3)
        self.play(FadeOut(RC))
        self.wait(1)
        with self.voiceover(text="To summarise, we found the half life for a radioisotope is equal to natural log of 2 over the decay constant and the half life for a capacitor discharging is natural log of 2 times the time constant. Hope this video helps and thanks for watching!") as tracker:
            half_life_eq_final.move_to(ORIGIN)  # Centers the equation
            self.play(Write(half_life_eq_final))
            rc_half_life_eq_final2.next_to(half_life_eq_final, DOWN)
            self.play(Write(rc_half_life_eq_final2))
            self.wait(5)
        self.play(FadeOut(half_life_eq_final), FadeOut(rc_half_life_eq_final2))


class HalfLife_under(VoiceoverScene):
    def construct(self):
        # Configure Azure voice service
        azure_service = AzureService(
            voice="en-GB-RyanNeural",
            style="newscast-casual",
        )
        self.set_speech_service(azure_service)

        # Title
        Title = Text("Half Life for Exponential Decay", font_size=48)
        with self.voiceover("In this video, we will derive expressions for the half life of a radioisotope in terms of its decay equation and for a capacitor, resistor series combination in terms of their time constant") as tracker:
            self.play(Write(Title))
            underline = Line(
                Title.get_left(), Title.get_right(), color=WHITE
            ).next_to(Title, DOWN)
            self.play(Create(underline))
            self.wait(2)
        self.play(FadeOut(Title), FadeOut(underline))

        # Radioisotope half life equations stacked vertically
        Radioisotope = Text("Radioisotope Half Life", font_size=36).to_edge(UP)
        decay_constant = MathTex(r"\lambda", font_size=36).next_to(Radioisotope, DOWN)
        decay_eq = MathTex(r"N(t) = N_0 e^{-\lambda t}", font_size=36).next_to(decay_constant, DOWN)
        half_life_eq = MathTex(r"N(t_{1/2}) = \frac{N_0}{2}", font_size=36).next_to(decay_eq, DOWN)
        half_life_eq_sub = MathTex(r"\frac{N_0}{2} = N_0 e^{-\lambda t_{1/2}}", font_size=36).next_to(half_life_eq, DOWN)
        half_life_eq_sub_div = MathTex(r"\frac{1}{2} = e^{-\lambda t_{1/2}}", font_size=36).next_to(half_life_eq_sub, DOWN)
        half_life_eq_sub_ln = MathTex(r"\ln\left(\frac{1}{2}\right) = -\lambda t_{1/2}", font_size=36).next_to(half_life_eq_sub_div, DOWN)
        half_life_eq_final = MathTex(r"t_{1/2} = \frac{\ln(2)}{\lambda}", font_size=36).next_to(half_life_eq_sub_ln, DOWN)

        with self.voiceover(text="""First, let's consider a radioisotope that decays over time. 
            The decay constant, lambda is the chance of an atom decaying per second. <bookmark mark='decayconstant'/> 
            All radioisotopes exhibit exponential decay and follow this decay equation <bookmark mark='exponetialdecay'/> 
            The half life of a radioisotope is defined as the time it takes for half of the atoms to decay. <bookmark mark='halflife'/> 
            Next we substitute t with t 1/2 and N(t) with N0/2 in the decay equation. <bookmark mark='sub'/> 
            To solve for t 1/2, we first divide both sides by N0 <bookmark mark='div'/> 
            and then take the natural log of both sides. <bookmark mark='ln'/> 
            Finally, we get our expression for half life. <bookmark mark='final'/>""") as tracker:
            
            self.play(Write(Radioisotope))
            self.wait_until_bookmark("decayconstant")
            self.play(Write(decay_constant))
            self.wait_until_bookmark("exponetialdecay")
            self.play(Write(decay_eq))
            self.wait_until_bookmark("halflife")
            self.play(Write(half_life_eq))
            self.wait_until_bookmark("sub")
            self.play(Write(half_life_eq_sub))
            self.wait_until_bookmark("div")
            self.play(Write(half_life_eq_sub_div))
            self.wait_until_bookmark("ln")
            self.play(Write(half_life_eq_sub_ln))
            self.wait_until_bookmark("final")
            self.play(Write(half_life_eq_final))
            self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # RC Circuit equations stacked vertically
        RC = Text("RC Circuit Half Life", font_size=36).to_edge(UP)
        time_constant = MathTex(r"\tau = RC", font_size=36).next_to(RC, DOWN)
        rc_eq = MathTex(r"Q(t) = Q_0 e^{-\frac{t}{RC}}", font_size=36).next_to(time_constant, DOWN)
        rc_half_life_eq = MathTex(r"Q(t_{1/2}) = \frac{Q_0}{2}", font_size=36).next_to(rc_eq, DOWN)
        rc_half_life_eq_sub = MathTex(r"\frac{Q_0}{2} = Q_0 e^{-\frac{t_{1/2}}{RC}}", font_size=36).next_to(rc_half_life_eq, DOWN)
        rc_half_life_eq_sub_div = MathTex(r"\frac{1}{2} = e^{-\frac{t_{1/2}}{RC}}", font_size=36).next_to(rc_half_life_eq_sub, DOWN)
        rc_half_life_eq_sub_ln = MathTex(r"\ln\left(\frac{1}{2}\right) = -\frac{t_{1/2}}{RC}", font_size=36).next_to(rc_half_life_eq_sub_div, DOWN)
        rc_half_life_eq_final = MathTex(r"t_{1/2} = RC \ln(2)", font_size=36).next_to(rc_half_life_eq_sub_ln, DOWN)
        rc_half_life_eq_final2 = MathTex(r"t_{1/2} = \tau \ln(2)", font_size=36).next_to(rc_half_life_eq_final, DOWN)

        with self.voiceover(text="""Now lets consider a capacitor discharging through a resistor.
            The time constant, tau, is resistance times capacitance. <bookmark mark='decayconstant'/> 
            For a discharging capacitor, the charge follows this equation. <bookmark mark='exponetialdecay'/> 
            We define half life as the time for charge to halve. <bookmark mark='halflife'/> 
            Substitute t with t 1/2 and Q(t) with Q0/2. <bookmark mark='sub'/> 
            Divide both sides by Q0 <bookmark mark='div'/> 
            Take natural log of both sides. <bookmark mark='ln'/> 
            Here's our final expression <bookmark mark='final'/> 
            which can be written in terms of tau. <bookmark mark='final2'/>""") as tracker:

            self.play(Write(RC))
            self.wait_until_bookmark("decayconstant")
            self.play(Write(time_constant))
            self.wait_until_bookmark("exponetialdecay")
            self.play(Write(rc_eq))
            self.wait_until_bookmark("halflife")
            self.play(Write(rc_half_life_eq))
            self.wait_until_bookmark("sub")
            self.play(Write(rc_half_life_eq_sub))
            self.wait_until_bookmark("div")
            self.play(Write(rc_half_life_eq_sub_div))
            self.wait_until_bookmark("ln")
            self.play(Write(rc_half_life_eq_sub_ln))
            self.wait_until_bookmark("final")
            self.play(Write(rc_half_life_eq_final))
            self.wait_until_bookmark("final2")
            self.play(Write(rc_half_life_eq_final2))
            self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
        summary_text = Text("Summary", font_size=48)
        with self.voiceover(text="To summarise, we found the half life for a radioisotope is equal to natural log of 2 over the decay constant and the half life for a capacitor discharging is natural log of 2 times the time constant. Hope this video helps and thanks for watching!") as tracker:
            self.play(Write(summary_text))
            self.wait(2)            
            half_life_eq_final.move_to(ORIGIN)  # Centers the equation
            self.play(Write(half_life_eq_final))
            rc_half_life_eq_final2.next_to(half_life_eq_final, DOWN)
            self.play(Write(rc_half_life_eq_final2))
            self.wait(5)
        self.play(FadeOut(summary_text), FadeOut(half_life_eq_final), FadeOut(rc_half_life_eq_final2))