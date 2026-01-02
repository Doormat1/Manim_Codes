from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class CurrentDerivation(VoiceoverScene):
    def construct(self):
        # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",
            style="newscast"
        ))

        # Create title screen
        title = Tex("Deriving the Drift Velocity Equation", font_size=48)
        subtitle = Tex(r"$I = nAve$", font_size=72)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)

        # Start with title screen and initial voiceover
        with self.voiceover(text="Let's derive the equation for drift velocity in a conductor.") as tracker:
            self.play(Write(title))
            self.wait(0.5)
            self.play(Write(subtitle))
            self.wait(1)
        
        # Clear title screen
        self.play(FadeOut(title_group))

        # Initial definitions with smaller font size
        definitions = VGroup(
            Tex(r"$n$ = number of charge carriers per unit volume", font_size=36),
            Tex(r"$e$ = charge per charge carrier", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=1).to_edge(UP, buff=1)

        # Total number of charge carriers equation
        N_equation = MathTex(
            r"N = nAl",
            font_size=36
        ).next_to(definitions, DOWN, buff=0.5).align_to(definitions, LEFT)

        # Total charge equation
        Q_equation = MathTex(
            r"Q = eN = enAl",
            font_size=36
        ).next_to(N_equation, DOWN, buff=0.5).align_to(definitions, LEFT)

        # Current equation with time
        I_equation_1 = MathTex(
            r"I = \frac{Q}{t} = enA", r"\frac{l}{t}",
            font_size=36
        ).next_to(Q_equation, DOWN, buff=0.5).align_to(definitions, LEFT)

        # Drift velocity definition
        v_equation = MathTex(
            r"v = \frac{l}{t}", r"\text{ (drift velocity)}",
            font_size=36
        ).next_to(I_equation_1, DOWN, buff=0.5).align_to(definitions, LEFT)

        # Final current equation
        final_equation = MathTex(
            r"I = nAve",
            font_size=36
        ).next_to(v_equation, DOWN, buff=0.5).align_to(definitions, LEFT)

        # Animation sequence with voiceover
        with self.voiceover(text="Let's derive the equation for drift velocity in a conductor.") as tracker:
            self.wait(1)

        with self.voiceover(text="We start with little n, the number of charge carriers per unit volume, and e, the charge per charge carrier.") as tracker:
            self.play(Write(definitions[0]))
            self.play(Write(definitions[1]))

        with self.voiceover(text="The total number of charge carriers, big n equals little n multiplied by the volume of the wire, which is the cross-sectional area A times the length l.") as tracker:
            self.play(Write(N_equation))

        with self.voiceover(text="The total charge Q equals the charge per charge carrier, e times by how many charge carriers we have, N, which gives us e n A l.") as tracker:
            self.play(Write(Q_equation))

        with self.voiceover(text="Current I is change in charge over change in time, so we get e n A l over t.") as tracker:
            self.play(Write(I_equation_1))

        with self.voiceover(text="The drift velocity v is defined as change in length over time.") as tracker:
            self.play(Write(v_equation))

        with self.voiceover(text="We can therefore substitute l over t with v.") as tracker:
            highlight_box_v = SurroundingRectangle(v_equation[0], color=YELLOW)
            highlight_box_I = SurroundingRectangle(I_equation_1[1], color=YELLOW)
            self.play(
                Create(highlight_box_v),
                Create(highlight_box_I)
            )
            self.wait(1)
            self.play(
                FadeOut(highlight_box_v),
                FadeOut(highlight_box_I)
            )

        with self.voiceover(text="This gives us our final equation: I equals n A v e.") as tracker:
            self.play(Write(final_equation))
            final_highlight = SurroundingRectangle(final_equation)
            self.play(Create(final_highlight))
            self.wait(1)