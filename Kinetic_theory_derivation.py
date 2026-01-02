from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class kinetictheoryderivation(VoiceoverScene):
    def construct(self):
        # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))
        
        # Create equations
        idealgasequation = MathTex(r"pV = nRT").scale(1.5)
        kinetictheoryequation = MathTex(r"p = \frac{1}{3} \rho \overline{c^2}").scale(1.5)
        densityequation = MathTex(r"\rho = \frac{m}{V}").scale(1.5)
        
        # Position equations side by side
        equation_group = VGroup(idealgasequation, kinetictheoryequation).arrange(RIGHT, buff=2)
        equation_group.to_edge(UP)
        
        # Position density equation below
        densityequation.next_to(kinetictheoryequation, DOWN, buff=1)
        
        # Rest of the equations remain the same
        massmolecularequation = MathTex(r"m = \frac{M}{N_A}").scale(1.5).to_edge(UP)
        combinedequation = MathTex(r"p = \frac{1}{3} \frac{M}{N_A V} \overline{c^2}").scale(1.5).to_edge(UP)
        finalequation = MathTex(r"pV = \frac{1}{3} N \overline{c^2} \frac{M}{N_A}").scale(1.5).to_edge(UP)  
        finalstep = MathTex(r"pV = \frac{2}{3} N \overline{E_k}").scale(1.5).to_edge(UP)
        
        title = Text("Derivation of the Ideal Gas Equation from Kinetic Theory").scale(0.7).to_edge(DOWN)
        self.play(Write(title))
        self.wait(2)
        
        # Show both equations simultaneously
        with self.voiceover(text="We start with the ideal gas equation, pV equals nRT, where p is pressure, V is volume, n is number of moles, R is the gas constant and T is temperature.") as tracker:
            self.play(
                Write(idealgasequation),
                FadeOut(title)
            )
        with self.voiceover(text="From kinetic theory, we have the equation p equals one third rho c squared, where rho is density and c squared is the mean square speed of the gas molecules.") as tracker:
            self.play(Write(kinetictheoryequation))
        self.wait(2)
        
        # Transform rho into m/V in the original kinetic theory equation position
        with self.voiceover(text="We can express density rho as mass m over volume V.") as tracker:
            self.play(Write(densityequation))
            # Create new kinetic theory equation with m/V instead of rho
            new_kinetictheoryequation = MathTex(r"p = \frac{1}{3} \frac{m}{V} \overline{c^2}").scale(1.5)
            new_kinetictheoryequation.move_to(kinetictheoryequation)
            self.play(
                Transform(kinetictheoryequation, new_kinetictheoryequation)
            )
        self.wait(2)

        with self.voiceover(text="The mass of a gas molecule m can be expressed as the molar mass M over Avogadro's number N A.") as tracker:
            self.play(Write(massmolecularequation.next_to(densityequation, DOWN)))
            # Create next transformation keeping position
            next_kinetic = MathTex(r"p = \frac{1}{3} \frac{M}{N_A V} \overline{c^2}").scale(1.5)
            next_kinetic.move_to(kinetictheoryequation)
            self.play(
                Transform(kinetictheoryequation, next_kinetic)
            )
        self.wait(2)

        with self.voiceover(text="Substituting the expressions for density and mass into the kinetic theory equation, we get p equals one third M over N A V times c squared.") as tracker:
            self.play(
                FadeOut(densityequation),
                FadeOut(massmolecularequation)
            )
            # Transform to show rearrangement
            next_step = MathTex(r"pV = \frac{1}{3} N \overline{c^2} \frac{M}{N_A}").scale(1.5)
            next_step.move_to(kinetictheoryequation)
            self.play(
                Transform(kinetictheoryequation, next_step)
            )
        self.wait(2)

        with self.voiceover(text="Rearranging this, we find that pV equals one third N c squared times M over N sub A, where N is the number of molecules.") as tracker:
            finalequation.move_to(kinetictheoryequation)
            self.play(
                FadeOut(kinetictheoryequation),
                FadeIn(finalequation)
            )
        self.wait(2)

        with self.voiceover(text="Since both equations represent the same pressure-volume relationship, we can equate them.") as tracker:
            # Create equation showing the equality
            combined = MathTex(r"nRT = \frac{1}{3} N \overline{c^2} \frac{M}{N_A}").scale(1.5)
            # Position the combined equation below the original equations
            combined.next_to(equation_group, DOWN, buff=1)
            

            
            self.play(
                Write(combined)
            )
            self.wait(1)
            
            # Move combined equation up to replace original equations
            self.play(
                FadeOut(idealgasequation),
                FadeOut(finalequation),
                combined.animate.move_to(equation_group)
            )
        self.wait(2)

        # Add kinetic energy equation
        kineticenergyequation = MathTex(r"Total E_k = \frac{1}{2}N M\overline{c^2}").scale(1.5)
        kineticenergyequation.to_edge(LEFT)

        # Add intermediate and final equations
        intermediate_eq = MathTex(r"\frac{3}{2}nRT = \frac{1}{2} N M\overline{c^2}").scale(1.5)
        final_ek_eq = MathTex(r"\frac{3}{2}nRT = E_k").scale(1.5)

        with self.voiceover(text="Finally, recognising that the total kinetic energy E k is half N M c squared bar, if we multiply both sides by 3/2, we can rewrite the equation as 3/2 N R T equals  N E sub k.") as tracker:
            # First show the kinetic energy equation
            self.play(Write(kineticenergyequation))
            self.wait(0.5)
            
            # Transform combined equation into intermediate form
            intermediate_eq.move_to(combined)
            self.play(
                Transform(combined, intermediate_eq)
            )
            self.wait(2)
            
            # Transform to final form with Ek
            final_ek_eq.move_to(combined)
            self.play(
                Transform(combined, final_ek_eq),
                FadeOut(kineticenergyequation)
            )
            self.wait(1)
        self.wait(2)       
        self.wait(0.5)

        # Create internal energy explanation
        internal_energy = MathTex(r"U = \sum E_p + \sum E_k").scale(1.5)
        ideal_gas_energy = MathTex(r"U = \sum E_k").scale(1.5)
        ideal_gas_text = Text("For an ideal gas, there are no potential energies", 
                            font_size=36).next_to(ideal_gas_energy, DOWN)

        with self.voiceover(text="For any gas, the internal energy U is the sum of potential and kinetic energies.") as tracker:
            self.play(
                Write(internal_energy)
            )
        self.wait(1)

        with self.voiceover(text="However, in an ideal gas there are no intermolecular forces, so there are no potential energies.") as tracker:
            self.play(
                Transform(internal_energy, ideal_gas_energy),
                Write(ideal_gas_text)
            )
        self.wait(2)
        with self.voiceover(text="Thus, for an ideal gas, the internal energy is simply the sum of the kinetic energies of all the molecules.") as tracker:
            # Transform existing equation into U = 3/2 nRT
            final_U_equation = MathTex(r"\frac{3}{2}nRT = U").scale(1.5)
            final_U_equation.move_to(combined)
            
            self.play(
                Transform(combined, final_U_equation)
            )
            self.wait(1)
        with self.voiceover(text="Now we have an equation for the total internal energy <bookmark mark='A'/>, if we divide by n, we get the internal energy per mole <bookmark mark='B'/> and finally if we change our energy definition to the average energy per molecule, we can get the internal energy per molecule instead <bookmark mark='C'/>") as tracker:
            # Clear previous equations
            self.play(
                FadeOut(ideal_gas_text),
                FadeOut(internal_energy),
                FadeOut(ideal_gas_energy),
            )
            
            # Create all equations first
            molar_energy_eq = MathTex(r"U = \frac{3}{2}RT").scale(1.5)
            molecular_energy_eq = MathTex(r"\overline{E_k} = \frac{3}{2}kT").scale(1.5)
            
            # Create labels
            total_label = Text("Total internal energy", font_size=24)
            molar_label = Text("Internal energy per mole", font_size=24)
            molecular_label = Text("Mean energy of a single molecule", font_size=24)
            
            # Position equations diagonally
            combined.to_corner(UL, buff=1)
            molecular_energy_eq.to_corner(DR, buff=1)
            
            
            # Position labels
            total_label.next_to(combined, DOWN)
            molecular_label.next_to(molecular_energy_eq, DOWN)

            # Calculate center position after other equations are positioned
            y_pos = (total_label.get_bottom()[1] + molecular_energy_eq.get_top()[1]) / 2
            molar_energy_eq.move_to(ORIGIN).shift(UP * y_pos)
            molar_label.next_to(molar_energy_eq, DOWN) #this label to be positioned after the move above is calculated.
            # Animate in sequence
            self.wait_until_bookmark("A")
            self.play(combined.animate.to_corner(UL, buff=1))
            self.play(FadeIn(total_label))
            
            
            self.wait_until_bookmark("B")
            self.play(
                FadeIn(molar_energy_eq),
                FadeIn(molar_label)
            )
            
            self.wait_until_bookmark("C")
            self.play(
                FadeIn(molecular_energy_eq),
                FadeIn(molecular_label)
            )
            
            self.wait(10)