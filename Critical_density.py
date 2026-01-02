from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
import numpy as np

class Critical(VoiceoverScene):
    def construct(self):
         # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))

        #Will start off discussing the fates of the universe with a graph
        axes = Axes([0,10,1], 
                    [0,8,1],
                    x_length = 8,
                    y_length= 6,
                    tips= True)
        x_label = axes.get_x_axis_label(Text("Time", font_size=20)).next_to(axes.x_axis.get_end(), DR)
        y_label = axes.get_y_axis_label(Text("Average Separation of Galaxies", font_size=20)).rotate(90*DEGREES).next_to(axes.y_axis, LEFT)
        graph_flat = axes.plot(lambda x: 4-2**(2-x), x_range= [0,10], use_smoothing = True, stroke_color = RED)
        graph_flat_label = axes.get_graph_label(
            graph_flat, 
            label="Flat",
            x_val=8,
            direction=UP
        ).shift(RIGHT*0.1)
        graph_closed = axes.plot(lambda x: (10*x-x**2)/6, x_range= [0,10], use_smoothing = True, stroke_color = GREEN)
        graph_closed_label = axes.get_graph_label(
            graph_closed, 
            label="Closed",
            x_val=8,
            direction=UP
        ).shift(RIGHT*0.5)
        
        graph_open = axes.plot(lambda x: np.log(x+1)*2.5, x_range=[0, 10], use_smoothing=True, stroke_color = BLUE)
        graph_open_label = axes.get_graph_label(
            graph_open, 
            label="Open",
            x_val=8,
            direction=UP
        ).shift(RIGHT*0.2)
        present_day = DashedLine(axes.coords_to_point(3,0), axes.coords_to_point(3,6))
        present_day_label = Text("Present Day", font_size=20).rotate(90*DEGREES).next_to(present_day,RIGHT,buff = 0.2).shift(DOWN)
        Graph_plot = VGroup(axes, x_label, y_label)
        Open_graph = VGroup(graph_open,graph_open_label)
        Closed_graph = VGroup(graph_closed, graph_closed_label)
        Flat_graph = VGroup(graph_flat, graph_flat_label)
        present_day_group = VGroup(present_day,present_day_label)
        Fate_graph = VGroup(Open_graph, Closed_graph, Flat_graph, Graph_plot,present_day_group)
        Flat_density = axes.get_graph_label(
            graph_flat, 
            label=MathTex(r"\rho = \rho_c"),
            x_val=8,
            direction=UP
        ).shift(RIGHT*0.1)
        Open_density = axes.get_graph_label(
            graph_open, 
            label=MathTex(r"\rho < \rho_c"),
            x_val=8,
            direction=UP
        ).shift(RIGHT*0.2)
        Closed_density = axes.get_graph_label(
            graph_closed,
            label = MathTex(r"\rho > \rho_c"),
            x_val= 8,
            direction=UP
        ).shift(RIGHT*0.5)
        Title = Text("Critical Density and the Fate of the Universe", font_size=36).to_edge(UP)
        title_underline = Underline(Title)
        Title_group = VGroup(Title, title_underline)

        
        with self.voiceover(text="""
            In this video we are going to look at the 3 possible fates for the universe and how we can use them to derive a forumla for the critical density of the unverise, where the fate flips from being closed to open. <bookmark mark="title"/>
            Lets look closer at the possible fates for the universe. We are going to plot a graph, <bookmark mark="graph"/> showing the average separation of galaxies against time. If we draw a line for the present day <bookmark mark="day"/> as well.
            There are three posibilities for the future of the universe. Firstly if we live in an open universe, where the universe keeps on expanding forever as the kinetic energy of the galaxies moving apart is greater than the gravitational potential energy trying to pull them together. <bookmark mark="open"/>                  
            Secondly if we live in a closed universe, the gravitational potential energy is greater than the kinetic energy, so the galaxies will reach a maximum expansion before gravity wins and pulls them back together it what is known as the big crunch. <bookmark mark="closed"/>
            Finally we could live in a flat universe, where gravitational potential energy and kinetic energy are balanced, meaning that the expansion continues on forever but it slows down until at inifitinate time, the galaxies stop moving. <bookmark mark="flat"/>     
            If we think about these in terms of the density of the universe. For a closed universe, its density is high, so greater than the crictical density. <bookmark mark="closedensity"/>
            In the open universe, the density is low, so the density is lower than the crtical density. <bookmark mark="opendensity"/>
            Finally in a flat universe, the density is just right and is equal to the critical density. <bookmark mark="flatdensity"/>
                            """)as tracker:
            self.play(Create(Title_group))
            self.wait_until_bookmark("title")
            self.play(Create(Graph_plot), Create(Open_graph), Create(Flat_graph))
            self.wait_until_bookmark("graph")
            self.play(Create(present_day_group))
            self.wait_until_bookmark("day")
            self.play(Create(Open_graph))
            self.wait_until_bookmark("open")
            self.play(Create(Closed_graph))
            self.wait_until_bookmark("closed")
            self.play(Create(Flat_graph))
            self.wait_until_bookmark("flat")
            self.play(Transform(graph_closed_label, Closed_density))
            self.wait_until_bookmark("closedensity")
            self.play(Transform(graph_open_label, Open_density))
            self.wait_until_bookmark("opendensity")
            self.play(Transform(graph_flat_label, Flat_density))
            self.wait_until_bookmark("flatdensity")
            self.wait(4)
        with self.voiceover(text="""
            Now lets look to use these definitions to derive a formula for the critical density. <bookmark mark="move"/>
            A quick recap of our definitions for each scenario. Open - Kinetic energy is greater than potential energy, Flat- kinetic energy is equal to potential energy and Closed - kinetic energy is less than potential energy. <bookmark mark="definitions"/>
            Now if we are defining critical density, the open and closed scenarios are no use to use, so lets remove them. <bookmark mark="remove"/>
            From our definition we get that potential energy is equal to kinetic energy, using our standard forumas we get this equation. <bookmark mark="energy"/>
            Hubble's law relates the velocity of a galaxy to its separation distance, so we can substitute this into our energy equation. <bookmark mark="hubble"/>
            From here, we can rearrange and group terms, cancelling one of the mass terms as we go. <bookmark mark="rearrange"/>
            Now to remove the term for the mass of the universe, we can think about the density of the universe. Assuming the universe is spherical in nature, we can get a forumla for the mass of the universe in terms of is radius and density. <bookmark mark="density"/>
            If we substitute this in, we can now rearrange our formula to get the critical density as the subject. <bookmark mark="criticaldensity"/>
            In our final piece of cancelling we get our formula for critical density to be, 3 8ths  times H naught squared, divided by big G times pi. <bookmark mark="finalequation"/>
            Now if we assume hubbles constant to be 70 kilometers per second per mega parsec, we get the a critical density to be 9.5 times 10 to the negative 27 kilograms per meter cubed, which is approximately 5 protons per cubic metre. 
            This is roughly what the observed density of the unverise is, so scientists currently think the flat future is the most likely. However all this work has large error bounds so there is much debate whether the universe is flat, open or closed. As the impact of dark matter and dark energy is further researched, these will also be included in this formula.
            Hopefully this video has helped with this derivation and thanks for watching.                
                        """) as tracker:
        #Now we look to derive formula
            self.play(Fate_graph.animate.scale(0.75).to_corner(UL))
            self.wait_until_bookmark("move")
            Forces_Open = Text("Open Universe - Expansion continues forever \n as the kinetic energy of the galaxies \n is greater than the potential energy \n pulling them in", font_size = 20).next_to (Fate_graph, RIGHT).shift(UP)
            self.play(Write(Forces_Open))
            self.wait(1)
            Forces_Flat = Text("Flat Universe - Expansion continues forever \n however it slows down until at \n infinite time expansion stops.\n Here the potential energy of a galaxy \n is equal to its kinetic energy", font_size= 20, should_center= False).next_to(Forces_Open, DOWN, buff = 0.2)
            self.play(Write(Forces_Flat))
            self.wait(1)
            Forces_Closed = Text("Closed Universe - Expansion continues to a \n certain point, after this the galaxies will start \n moving towards each other. \n Here the potential energy of the galaxies \n is greater than their kinetic energy", font_size=20,  should_center= False).next_to(Forces_Flat, DOWN, buff = 0.2)
            self.play(Write(Forces_Closed))
            self.wait_until_bookmark("definitions")
            self.play(Unwrite(Forces_Open), Unwrite(Forces_Closed))
            self.play(Forces_Flat.animate.shift(UP*1.5))
            self.wait_until_bookmark("remove")
            equal_energies = MathTex(r"E_P=E_k").next_to(Forces_Flat, DOWN, buff = 0.2)
            equal_energies2= MathTex(r"\frac{GM_1 M_2}{r}= \frac{1}{2}mv^2").next_to(equal_energies, DOWN, buff = 0.2)
            hubble_law = MathTex(r"v= H_o R").next_to(equal_energies2, DOWN, buff = 0.2)
            equal_energies_hubblesub = MathTex(r"\frac{GM_1 M_2}{r}= \frac{1}{2}m H_o^2 r^2").next_to(equal_energies, DOWN, buff = 0.2)
            equal_energies_cancel = MathTex(r"G M= \frac{1}{2} H_o^2 r^3").next_to(equal_energies, DOWN, buff = 0.2)
            density = MathTex(r"m = V \rho").next_to(equal_energies2,DOWN, buff = 0.2)
            density_volume_formula =MathTex(r"m = \frac{4}{3} \pi r^3 \rho").next_to(equal_energies2,DOWN, buff = 0.2)
            critical_density_initial = MathTex(r"G \frac{4}{3} \pi r^3 \rho= \frac{1}{2} H_o^2 r^3").next_to(equal_energies, DOWN, buff = 0.2)
            critical_density_final = MathTex(r"\rho_c= \frac{3 H_o^2 }{8 G \pi}").next_to(critical_density_initial, DOWN, buff = 0.2)
            self.play(Write(equal_energies))
            self.wait(1)
            self.play(Write(equal_energies2))
            self.wait_until_bookmark("energy")
            self.play(Write(hubble_law))
            self.wait(1)
            self.play(FadeOut(equal_energies2), FadeIn (equal_energies_hubblesub))
            self.wait_until_bookmark("hubble")
            self.play(FadeOut(equal_energies_hubblesub),FadeIn(equal_energies_cancel))
            self.wait_until_bookmark("rearrange")
            self.play(FadeOut(hubble_law), FadeIn (density))
            self.wait(2)
            self.play(Transform(density, density_volume_formula))
            self.wait_until_bookmark("rearrange")
            self.play(FadeOut(equal_energies_cancel),FadeIn (critical_density_initial))
            self.wait_until_bookmark("criticaldensity")
            self.play(FadeOut(density), FadeIn(critical_density_final))
            self.wait_until_bookmark("finalequation")
            critical_density_example = Tex(
                r"If the current value of $H_0$ is 70 km s$^{-1}$ Mpc$^{-1}$, \\ this gives us a critical density of $9.5 \times 10^{-27}$ kg m$^{-3}$. \\ This is roughly equivalent to 5 hydrogen nuclei (protons) per cubic metre"
                , font_size = 30).next_to(Fate_graph, DOWN).shift(RIGHT)
            self.play(Write(critical_density_example))
            self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
        
        
