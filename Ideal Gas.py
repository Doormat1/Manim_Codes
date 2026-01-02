from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class IdealGasAnimation(VoiceoverScene):
    def construct(self):
        # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))

        # The question text with line wrapping, aligned to top
        question_text = Text(
            "A gas has a volume of 2.0 m³ at a pressure of 100 kPa and a temperature of 300 K.\n"
            "If the pressure is increased to 200 kPa while the temperature remains constant,\n"
            "what is the new volume of the gas?\n"
            "\n"
            "Step 1 List the Key Terms"
        ).scale(0.5).to_edge(UP)

        with self.voiceover(text="Let's solve this ideal gas problem step by step.") as tracker:
            self.play(Write(question_text))
        self.wait(2)

        # Extract values
        p1 = 100
        v1 = 2.0
        t1 = 300
        p2 = 200
        t2 = 300

        # Create MathTex objects for the list, placed below the question
        p1_text = MathTex(r"p_1 = {} \, \text{{kPa}}".format(p1)).next_to(question_text, DOWN, buff=1).to_edge(LEFT).set_color(YELLOW)
        v1_text = MathTex(r"V_1 = {} \, \text{{m}}^3".format(v1)).next_to(p1_text, DOWN, aligned_edge=LEFT).set_color(YELLOW)
        t1_text = MathTex(r"t_1 = {} \, \text{{K}}".format(t1)).next_to(v1_text, DOWN, aligned_edge=LEFT).set_color(YELLOW)
        p2_text = MathTex(r"p_2 = {} \, \text{{kPa}}".format(p2)).next_to(p1_text, RIGHT, buff=2).set_color(YELLOW)
        t2_text = MathTex(r"t_2 = {} \, \text{{K}}".format(t2)).next_to(p2_text, DOWN, aligned_edge=LEFT).set_color(YELLOW)
        v2_text = MathTex(r"V_2 = ?").next_to(t2_text, DOWN, aligned_edge=LEFT).set_color(YELLOW)

        with self.voiceover(text="First, let's identify the key terms from the question. ") as tracker:
            # Animate the values moving from the question to the list
            question_text[34:40].set_color(YELLOW)  # Highlight p1
            self.wait(0.5)
        with self.voiceover(text="p1 = 100 kilo pascals, v1 = 2 cubic metres, t1 = 300 kelvin, p2 = 200 kilo pascals, t2 = 300 kelvin as the temperature is constant, v2 is our unknown.") as tracker:     
            self.play(Transform(question_text[34:40].copy(), p1_text), run_time=2) #p1
            question_text[34:40].set_color(WHITE)  # Change back to white
            self.wait(0.5)
            question_text[16:21].set_color(YELLOW)  # Highlight v1
            self.play(Transform(question_text[16:21].copy(), v1_text), run_time=2) #v1
            question_text[16:21].set_color(WHITE)  # Change back to white
            self.wait(0.5)
            question_text[57:62].set_color(YELLOW)  # Highlight t1
            self.play(Transform(question_text[57:62].copy(), t1_text), run_time=2) #t1
            question_text[57:62].set_color(WHITE)  # Change back to white
            self.wait(0.5)
            question_text[88:94].set_color(YELLOW)  # Highlight p2
            self.play(Transform(question_text[88:94].copy(), p2_text), run_time=2) #p2
            question_text[88:94].set_color(WHITE)  # Change back to white
            self.wait(0.5)
            question_text[102:129].set_color(YELLOW)  # Highlight t2
            self.play(Transform(question_text[102:129].copy(), t2_text), run_time=2) #t2
            question_text[102:129].set_color(WHITE)  # Change back to white
            self.wait(0.5)
            self.play(Write(v2_text.set_color(YELLOW)))
            self.wait(2)

        with self.voiceover(text="Now that we have our values listed, let's write down the equation.") as tracker:
            step1_text = question_text[-20:]  # Select the last 20 characters of question_text
            step2_text = Text("Step 2 Substitute In").scale(0.5).move_to(step1_text.get_center()).align_to(step1_text, LEFT)
            self.play(ReplacementTransform(step1_text, step2_text))

        with self.voiceover(text="Remember as p times v divided by t is constant we can write the equation as p1v1 over t1 = p2v2 over t2") as tracker:
            equation = MathTex(r"\frac{p_1 V_1}{t_1} = \frac{p_2 V_2}{t_2}").next_to(v2_text, DOWN, buff=1)
            self.play(Write(equation))

        with self.voiceover(text="Let's substitute our known values into the equation.") as tracker:
            substituted_equation = MathTex(
                r"\frac{{{} \cdot {}}}{{{}}} = \frac{{{} \cdot V_2}}{{{}}}".format(p1, v1, t1, p2, t2)
            ).move_to(equation.get_center())
            self.play(Transform(equation, substituted_equation))

        with self.voiceover(text="Now we can solve for V2.") as tracker:
            step3_text = Text("Step 3 Solve for V2").scale(0.5).move_to(step2_text.get_center()).align_to(step2_text, LEFT)
            self.play(ReplacementTransform(step2_text, step3_text))

        with self.voiceover(text="Rearranging the equation to isolate V2...") as tracker:
            v2 = p1 * v1 * t2 / (p2 * t1)
            solved_equation = MathTex(r"V_2 = \frac{{{} \cdot {} \cdot {}}}{{{} \cdot {}}}".format(p1, v1, t2, p2, t1)).move_to(equation.get_center())
            self.play(Transform(equation, solved_equation))

        with self.voiceover(text="Finally, let's calculate the value of V2.") as tracker:
            step4_text = Text("Step 4 Calculate V2").scale(0.5).move_to(step3_text.get_center()).align_to(step3_text, LEFT)
            self.play(ReplacementTransform(step3_text, step4_text))
        
        with self.voiceover(text=f"The new volume is {v2} cubic meters.") as tracker:
            v2_value = MathTex(r"V_2 = \frac{{{} \cdot {} \cdot {}}}{{{} \cdot {}}} = {} \, \text{{m}}^3".format(p1, v1, t2, p2, t1, v2)).move_to(equation.get_center())
            self.play(Transform(equation, v2_value))
            self.wait(2)







