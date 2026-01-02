from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

# Check for Azure credentials

class Capacitors_in_series_and_parallel(VoiceoverScene):
    def construct(self):
        # Configure Azure voice service
        azure_service = AzureService(
            voice="en-GB-RyanNeural",
            style="newscast-casual",
        )
        self.set_speech_service(azure_service)
        # Title
        Title = Text("Capacitors in Series and Parallel", font_size=48)
        with self.voiceover("In this video, we will explore capacitors connected in series and parallel configurations. We will derive the formulas for equivalent capacitance in both cases and provide examples to illustrate these concepts.") as tracker:
            self.play(Write(Title))
            # Add underline under the title
            underline = Line(
                Title.get_left(), Title.get_right(), color=WHITE
            ).next_to(Title, DOWN)
            self.play(Create(underline))
            self.wait(2)
        self.play(FadeOut(Title), FadeOut(underline))
        # Series Capacitors
        Series_Title = Text("Capacitors in Series", font_size=42)
        with self.voiceover("Let's start with capacitors in series. ") as tracker:
            self.play(Write(Series_Title))
            self.wait(2)
        self.play(FadeOut(Series_Title))
        # Diagram for Series Capacitors
        # Each capacitor: two parallel coloured plates, wires between, label underneath

        # Capacitor plates
        c1_plates = VGroup(
            Line([0, 0.2, 0], [0, 0.8, 0], color=BLUE, stroke_width=8),
            Line([0.2, 0.2, 0], [0.2, 0.8, 0], color=BLUE, stroke_width=8),
        )
        c2_plates = VGroup(
            Line([1, 0.2, 0], [1, 0.8, 0], color=GREEN, stroke_width=8),
            Line([1.2, 0.2, 0], [1.2, 0.8, 0], color=GREEN, stroke_width=8),
        )
        c3_plates = VGroup(
            Line([2, 0.2, 0], [2, 0.8, 0], color=RED, stroke_width=8),
            Line([2.2, 0.2, 0], [2.2, 0.8, 0], color=RED, stroke_width=8),
        )

        # Wires between capacitors
        wires = VGroup(
            Line([-0.4, 0.5, 0], [0, 0.5, 0], color=WHITE, stroke_width=4),    # left wire
            Line([0.2, 0.5, 0], [1, 0.5, 0], color=WHITE, stroke_width=4),     # wire between c1 and c2
            Line([1.2, 0.5, 0], [2, 0.5, 0], color=WHITE, stroke_width=4),     # wire between c2 and c3
            Line([2.2, 0.5, 0], [2.6, 0.5, 0], color=WHITE, stroke_width=4),   # right wire
        )

        # Labels below each capacitor
        c1_label = MathTex("C_1", font_size=24).next_to(c1_plates, DOWN)
        c2_label = MathTex("C_2", font_size=24).next_to(c2_plates, DOWN)
        c3_label = MathTex("C_3", font_size=24).next_to(c3_plates, DOWN)

        # Q labels
        q1_label = MathTex("Q", font_size=24).next_to(c1_label, DOWN)
        q2_label = MathTex("Q", font_size=24).next_to(c2_label, DOWN)
        q3_label = MathTex("Q", font_size=24).next_to(c3_label, DOWN)

        # Voltage labels
        v1_label = MathTex("V_1", font_size=24).next_to(c1_plates, UP)
        v2_label = MathTex("V_2", font_size=24).next_to(c2_plates, UP)
        v3_label = MathTex("V_3", font_size=24).next_to(c3_plates, UP)

        # Group all and position
        series_diagram = VGroup(
            c1_plates, c1_label,
            c2_plates, c2_label,
            c3_plates, c3_label,
            wires
        )
        series_diagram.move_to(UP * 2)
        with self.voiceover("Here we have three capacitors connected in series.") as tracker:
            self.play(Create(series_diagram))
            self.wait(2)
            
        # Create current arrow and Q labels
        current_arrow = Arrow(
            start=[-1.6, 0.5, 0],  # Moved start point to align with C1
            end=[-0.6, 0.5, 0],     # Adjusted end point accordingly
            color=YELLOW,
            buff=0
        ).scale(1)
        
        current_label = Text("I", font_size=24).next_to(current_arrow, UP)
        
        # Define Q labels
        q1_label = Text("Q", font_size=24).next_to(c1_label, DOWN )
        q2_label = Text("Q", font_size=24).next_to(c2_label, DOWN )
        q3_label = Text("Q", font_size=24).next_to(c3_label, DOWN )
        
        # Animate arrow moving and Q labels appearing
        with self.voiceover(
            text=""" In a series configuration, the same current flows through all the capacitors, therefore they store the same charge. <bookmark mark='Q'/> 
            However, the voltage across each capacitor can be different and is given by V = Q/C.<bookmark mark='V'/> 
        """) as tracker:
            self.play(
                Create(current_arrow),
                Create(current_label)
            )
            self.play(
                current_arrow.animate.shift(RIGHT ),
                current_label.animate.shift(RIGHT ),
                Write(q1_label)
            )
            # Move arrow past C2 and show Q2
            self.play(
                current_arrow.animate.shift(RIGHT),
                current_label.animate.shift(RIGHT),
                Write(q2_label)
            )
            # Move arrow past C3 and show Q3
            self.play(
                current_arrow.animate.shift(RIGHT),
                current_label.animate.shift(RIGHT),
                Write(q3_label)
            )
            self.wait_until_bookmark("Q")
            self.wait(1)
        # Remove arrow
            self.play(
                FadeOut(current_arrow),
                FadeOut(current_label),
            )

        # Continue with voltage and charge labels
        # Voltage and Charge in Series Capacitors

            # Voltage labels
            v1_label = Text("V1", font_size=24).next_to(c1_plates, UP)
            v2_label = Text("V2", font_size=24).next_to(c2_plates, UP)
            v3_label = Text("V3", font_size=24).next_to(c3_plates, UP)
            v1_calculation = MathTex("V_1 = \\frac{Q}{C_1}", font_size=24).next_to(q1_label, DOWN)
            v2_calculation = MathTex("V_2 = \\frac{Q}{C_2}", font_size=24).next_to(q2_label, DOWN)
            v3_calculation = MathTex("V_3 = \\frac{Q}{C_3}", font_size=24).next_to(q3_label, DOWN)
            self.play(Write(v1_label), Write(v2_label), Write(v3_label), Write(v1_calculation), Write(v2_calculation), Write(v3_calculation))
            self.wait_until_bookmark("V")
            self.wait(2)            
        # Deriving the Formula for Equivalent Capacitance in Series

        with self.voiceover(text="""
            Now we know the voltage across each capacitor and in a series circuit, that the sum of the voltages across each component equals the supply voltage. <bookmark mark='seriesvoltage'/> 
            We can now substitute our 3 equations for the voltage into this relationship. <bookmark mark='substitution'/>
            Next we divide through by Q <bookmark mark='divide'/>

            This gives us 1 over the equivalent capacitance on the left hand side <bookmark mark='1over'/>
            And the sum of the reciprocals of each individual capacitance on the right hand side. <bookmark mark='sum'/>
            So in a series circuit, the reciprocal of the equivalent capacitance is equal to the sum of the reciprocals of each individual capacitance. <bookmark mark='final'/>
        """) as tracker:
        # Charge and Voltage Diagram for Derivation
            v_series = MathTex("V = V_1 + V_2 + V_3", font_size=36).next_to(v2_calculation, DOWN * 2)
            self.play(Write(v_series))
            self.wait_until_bookmark("seriesvoltage")
            v_substitution = MathTex("V_T = \\frac{Q}{C_1} + \\frac{Q}{C_2} + \\frac{Q}{C_3}", font_size=36).move_to(v_series)
            self.play(Transform(v_series, v_substitution))
            self.wait_until_bookmark("substitution")
            v_divide = MathTex("\\frac{V_T}{Q} = \\frac{1}{C_1} + \\frac{1}{C_2} + \\frac{1}{C_3}", font_size=36).move_to(v_series)
            self.play(Transform(v_series, v_divide))
            self.wait_until_bookmark("divide")
            v_1over = MathTex("\\frac{1}{C_{eq}} = \\frac{1}{C_1} + \\frac{1}{C_2} + \\frac{1}{C_3}", font_size=36).move_to(v_series)
            self.play(Transform(v_series, v_1over))
            self.wait_until_bookmark("sum")
            self.wait_until_bookmark("final")
            self.wait(2)
            self.play(FadeOut(v_series))
            self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Examples for Series Capacitors
        example_title = Text("Examples for Series Capacitors", font_size=36)
        with self.voiceover(
            text = """Let's go through an example to solidify our understanding of capacitors in series. <bookmark mark='title'/> Consider three capacitors in series with capacitances C1, C2, and C3.""") as tracker:
            self.play(Write(example_title))
            self.wait(1)
            self.play(example_title.animate.to_edge(UP))
            self.wait_until_bookmark('title')
            self.play(Create(series_diagram)) # Reuse the series diagram
        
        self.wait(2)
        # Given Values for Example
        c1_given = MathTex(r"2\mu F", font_size=24).next_to(c1_plates, DOWN)
        c2_given = MathTex(r"3\mu F", font_size=24).next_to(c2_plates, DOWN)
        c3_given = MathTex(r"6\mu F", font_size=24).next_to(c3_plates, DOWN)

        with self.voiceover("In this example, we have three capacitors with capacitances 2 microfarads, 3 microfarads, and 6 microfarads. Let's find the equivalent capacitance using the formula we derived.") as tracker:
            self.play(Transform(c1_label, c1_given), Transform(c2_label, c2_given), Transform(c3_label, c3_given))
            self.wait(2)
        # Calculating Equivalent Capacitance for Example
        calc_eq_capacitance = MathTex(r"\frac{1}{C_{eq}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3}", font_size=36)
        sub_eq_capacitance = MathTex(r"\frac{1}{C_{eq}} = \frac{1}{2\mu} + \frac{1}{3\mu} + \frac{1}{6\mu}", font_size=36)
        
        with self.voiceover(text="""Substituting the values into the formula, <bookmark mark='sub'/> we get 1 over C eq equals 1 over 2 plus 1 over 3 plus 1 over 6. Solving this equation gives us the value of the equivalent capacitance.""") as tracker:
            self.play(Write(calc_eq_capacitance))
            self.wait_until_bookmark('sub')
            self.play(Transform(calc_eq_capacitance, sub_eq_capacitance))
        
        # Result for Equivalent Capacitance
        result_1_over_capacitance = MathTex(r"\frac{1}{C_{eq}} = 1000000", font_size=36)
        result_eq_capacitance = MathTex(r"C_{eq} = 1\mu F", font_size=36)
        with self.voiceover(text = """Using a calculator, we work out that 1 over the capacitance = 1 million, <bookmark mark='1overC'/> so therefore the capacitance = 1 micro farad """ ) as tracker:
            self.play(Transform(calc_eq_capacitance, result_1_over_capacitance))
            self.wait_until_bookmark('1overC')
            self.play(Transform(calc_eq_capacitance,result_eq_capacitance))
            self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Parallel Capacitors
        parallel_title = Text("Capacitors in Parallel", font_size=42)
        with self.voiceover("Now, let's move on to capacitors in parallel. In a parallel configuration, the voltage across each capacitor is the same, but the charge can be different.") as tracker:
            self.play(Write(parallel_title))
            self.wait(2)
        self.play(FadeOut(parallel_title))
        # Diagram for Parallel Capacitors
        # Capacitor plates (arranged vertically with common bus bars)
        
        # Bus bars (vertical lines on sides)
        left_bus = Line([0, 3.0, 0], [0, 0, 0], color=WHITE, stroke_width=4)
        right_bus = Line([2, 3.0, 0], [2, 0, 0], color=WHITE, stroke_width=4)

        # Capacitor plates with connecting wires (rotated 90 degrees)
        cp1_plates = VGroup(
            Line([0.9, 2.0, 0], [0.9, 2.8, 0], color=BLUE, stroke_width=8),   # left plate
            Line([1.1, 2.0, 0], [1.1, 2.8, 0], color=BLUE, stroke_width=8),   # right plate
            Line([0, 2.4, 0], [0.9, 2.4, 0], color=WHITE, stroke_width=4),    # left wire
            Line([1.1, 2.4, 0], [2, 2.4, 0], color=WHITE, stroke_width=4),    # right wire
        )

        cp2_plates = VGroup(
            Line([0.9, 0.8, 0], [0.9, 1.6, 0], color=GREEN, stroke_width=8),  # left plate
            Line([1.1, 0.8, 0], [1.1, 1.6, 0], color=GREEN, stroke_width=8),  # right plate
            Line([0, 1.2, 0], [0.9, 1.2, 0], color=WHITE, stroke_width=4),    # left wire
            Line([1.1, 1.2, 0], [2, 1.2, 0], color=WHITE, stroke_width=4),    # right wire
        )

        cp3_plates = VGroup(
            Line([0.9, -0.4, 0], [0.9, 0.4, 0], color=RED, stroke_width=8),   # left plate
            Line([1.1, -0.4, 0], [1.1, 0.4, 0], color=RED, stroke_width=8),   # right plate
            Line([0, 0.0, 0], [0.9, 0.0, 0], color=WHITE, stroke_width=4),    # left wire
            Line([1.1, 0.0, 0], [2, 0.0, 0], color=WHITE, stroke_width=4),    # right wire
        )

        # Labels for each capacitor (V and Q side by side)
        cp1_labels = VGroup(
            MathTex("C_1", font_size=24),
        ).arrange(RIGHT, buff=0.5).next_to(cp1_plates, RIGHT)

        cp2_labels = VGroup(
            MathTex("C_2", font_size=24),
        ).arrange(RIGHT, buff=0.5).next_to(cp2_plates, RIGHT)

        cp3_labels = VGroup(
            MathTex("C_3", font_size=24),
        ).arrange(RIGHT, buff=0.5).next_to(cp3_plates, RIGHT)

        # Group all elements (without the charge labels for now)
        parallel_diagram = VGroup(
            left_bus, right_bus,
            cp1_plates, cp2_plates, cp3_plates,
            cp1_labels, cp2_labels, cp3_labels
        )

        parallel_diagram.move_to(ORIGIN)
        self.play(Create(parallel_diagram))
        self.wait(2)

        # Voltage and Charge in Parallel Capacitors
        with self.voiceover("In a parallel configuration, the voltage across each capacitor is the same and is equal to the total voltage. The charge on each capacitor can be different and is calculated by using Q = CV.") as tracker:
            # First create voltage labels
            vp1_label = MathTex("V", font_size=24).next_to(cp1_plates, UP)
            vp2_label = MathTex("V", font_size=24).next_to(cp2_plates, UP)
            vp3_label = MathTex("V", font_size=24).next_to(cp3_plates, UP)
            self.play(Write(vp1_label), Write(vp2_label), Write(vp3_label))
            self.wait(2)
            # Now create charge labels after voltage labels exist
            cq1_label = MathTex("Q_1", font_size=24).next_to(vp1_label, RIGHT)
            cq2_label = MathTex("Q_2", font_size=24).next_to(vp2_label, RIGHT)
            cq3_label = MathTex("Q_3", font_size=24).next_to(vp3_label, RIGHT)
            self.play(Write(cq1_label), Write(cq2_label), Write(cq3_label))
            self.wait(2)
            parallel_diagram.add(vp1_label, vp2_label, vp3_label, cq1_label, cq2_label, cq3_label)
            self.play(parallel_diagram.animate.move_to(LEFT))
        # Deriving the Formula for Equivalent Capacitance in Parallel
        qtotal = MathTex("Q_T = Q_1 + Q_2 + Q_3", font_size=36).next_to(parallel_diagram, RIGHT)
        parallel_divide = MathTex(r"\frac{Q_T}{V} = \frac{Q_1}{V} + \frac{Q_2}{V} + \frac{Q_3}{V}", font_size=36).next_to(parallel_diagram, RIGHT)
        with self.voiceover(text = """We know that the total current in the circuit is the sum of the currents in each branch. <bookmark mark='qt'/> Therefore the total charge in our circuit is the sum of the charges across each capacitor. <bookmark mark='divide'/> If we divide by the voltage across each capacitor, which is the same, we get capacitance.""") as tracker:
            self.wait_until_bookmark('qt')
            self.play(Write(qtotal))
            self.wait_until_bookmark('divide')
            self.play(Transform(qtotal, parallel_divide))
            self.wait(2)
        final_formula_parallel = MathTex("C_{eq} = C_1 + C_2 + C_3", font_size=36).next_to(parallel_diagram, RIGHT)
        with self.voiceover("Finally we get our formula for the equivalent capacitance for capacitors in pararllel, where Ceq = C1+C2+C3. ") as tracker:
            self.play(Transform(qtotal,final_formula_parallel))
            self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        # Examples for Parallel Capacitors
        example_parallel_title = Text("Examples for Parallel Capacitors", font_size=36)
        with self.voiceover("Let's go through some examples to solidify our understanding of capacitors in parallel. Consider three capacitors in parallel with capacitances C1, C2, and C3. Let's find the equivalent capacitance.") as tracker:
            self.play(Write(example_parallel_title))
            self.wait(2)
        self.play(FadeOut(example_parallel_title))
        parallel_diagram.remove(vp1_label, vp2_label, vp3_label, cq1_label, cq2_label, cq3_label) # Remove voltage labels and charge labels
        self.play(Create(parallel_diagram))
        self.play(parallel_diagram.animate.move_to([-5, 0, 0]))
        self.wait(2)
        # Given Values for Example
        c1_given_parallel = MathTex(r"2\mu F", font_size=24).next_to(cp1_plates, RIGHT)
        c2_given_parallel = MathTex(r"3\mu F", font_size=24).next_to(cp2_plates, RIGHT)
        c3_given_parallel = MathTex(r"6\mu F", font_size=24).next_to(cp3_plates, RIGHT)
        with self.voiceover("In this example, we have three capacitors with capacitances 2 microfarads, 3 microfarads, and 6 microfarads. Let's find the equivalent capacitance using the formula we derived.") as tracker:
            self.play(Transform(cp1_labels, c1_given_parallel), Transform(cp2_labels, c2_given_parallel), Transform(cp3_labels, c3_given_parallel))
            self.wait(2)
        # Calculating Equivalent Capacitance for Example
        calc_eq_capacitance_parallel = MathTex("C_{eq} = 2\mu + 3\mu + 6\mu", font_size=36)
        with self.voiceover("Substituting the values into the formula, we get Ceq equals 2 plus 3 plus 6. Solving this equation gives us the value of the equivalent capacitance.") as tracker:
            self.play(Write(calc_eq_capacitance_parallel))
            self.wait(2)
        self.play(FadeOut(calc_eq_capacitance_parallel))
        # Result for Equivalent Capacitance
        result_eq_capacitance_parallel = MathTex("C_{eq} = 11\mu F", font_size=36)
        with self.voiceover("Therefore, the equivalent capacitance of the given capacitors in parallel is 11 microfarads.") as tracker:
            self.play(Write(result_eq_capacitance_parallel))
            self.wait(2)
        self.play(FadeOut(result_eq_capacitance_parallel))
        # Conclusion
        conclusion_title = Text("Conclusion", font_size=36)
        with self.voiceover("In conclusion, we have explored capacitors connected in series and parallel configurations. We derived the formulas for equivalent capacitance in both cases and worked through examples to illustrate these concepts. Understanding these principles is essential for analyzing and designing electrical circuits.") as tracker:
            self.play(Write(conclusion_title))
            self.wait(2)
        self.play(FadeOut(conclusion_title))
        # End
        end_title = Text("Thank you for watching!", font_size=36)
        with self.voiceover("Thank you for watching this video on capacitors in series and parallel. We hope you found it informative and helpful. Don't forget to like, share, and subscribe for more educational content.") as tracker:
            self.play(Write(end_title))
            self.wait(2)
        self.play(FadeOut(end_title))
        self.wait(1)
