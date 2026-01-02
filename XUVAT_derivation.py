from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class Equation(VoiceoverScene):
    def construct(self):
    # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
        voice="en-GB-RyanNeural",
        style="newscast"
    ))
    # Create the title
        title = Text("Deriving XUVAT Equations", font_size=72, color=YELLOW)
        subtitle = Text("Equations of Constant Acceleration Explained", font_size=36, color=BLUE)
    
    # Positioning the title and subtitle
        title.shift(UP * 1)
        subtitle.next_to(title, DOWN)
        with self.voiceover(text="Let's derive the equations of motion for constant acceleration, also known as the X UVAT equations.") as tracker:
        # Animations
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=2)
    
        # Add some decoration (optional)
            underline = Line(LEFT, RIGHT, color=WHITE).scale(4)
            underline.next_to(subtitle, DOWN)
    
            self.play(Create(underline), run_time=2)
    
        # Hold the final frame
            self.wait(5)
            self.play(FadeOut(title, subtitle, underline), run_time=2)
    
    # Define the terms 
        lines = VGroup(
            Tex(r"$x\ =\ displacement\ in\ m\ (this\ is\ s\ for\ other\ boards)$"),
            Tex(r"$u\ =\ initial\ velocity\ in\ ms^{-1},\ when\ time\ =\ 0s$"),
            Tex(r"$v\ =\ final\ velocity\ in\ ms^{-1},\ when\ time\ =\ maximum\ value$"),
            Tex(r"$a\ =\ acceleration\ in\ ms^{-2}$"),
            Tex(r"$t\ =\ time\ in\ seconds\ (the\ only\ scalar\ quantity\ here)$"),
        )
        lines.font_size = 40
        lines.arrange(DOWN)

        with self.voiceover(
            text="""1st step is to define our terms. 
            Our first term is x, for displacement in meters, for most exam boards including WJEC Maths, this is an s. 
            <bookmark mark='line1'/>
            Next is u, the initial velocity in meters per second when time equals zero.
            <bookmark mark='line2'/>
            Then v, the final velocity in meters per second at maximum time.
            <bookmark mark='line3'/>
            We have a, acceleration in meters per second squared.
            <bookmark mark='line4'/>
            And finally t, time in seconds, the only scalar quantity here.
            <bookmark mark='line5'/>"""
        ) as tracker:
            # Animate first line immediately
            self.play(Write(lines[0], run_time=2))
    
        # Wait for each bookmark, then animate the next line
            for i, mark in enumerate(['line1', 'line2', 'line3', 'line4']):
                self.wait_until_bookmark(mark)
                self.play(Write(lines[i + 1], run_time=2))

            self.wait(3)  # Pause for 3 seconds at the end
            self.clear()
    
        t1 = Tex(r"$a=$", r"$\frac{\Delta v}{\Delta t}$", font_size=96)
        t2 = Tex(r"$a =$", r"$\frac{v-u}{\Delta t}$", font_size=96)
        t3 = Tex(r"$v=$", r"$u+at$", r"$\ \ (1)$", font_size=96)
        g = VGroup(t1, t2, t3).arrange(DOWN, aligned_edge=LEFT, buff=1)
        equation1 = Tex(r"$v=u+at$", r"$\ \ (1)$", font_size=96)
        equation2 = Tex(r"$x= \frac{u+v}{2}t$", r"$\ \ (2)$", font_size=96)
        equation1.shift(UP * 3)
        equation2.next_to(equation1, DOWN)
        with self.voiceover(
            text="""On to the actual derivation.
            From definition, acceleration equals change in velocity over change in time. 
            <bookmark mark='line1'/>
            We can rewrite change in velocity as final velocity minus initial velocity.
            <bookmark mark='line2'/>
            If we rearrange this equation to make v the subject, we get v equals u plus a t.
            <bookmark mark='line3'/>
            This gives us our first equation, equation one, v equals u plus a t."""
        ) as tracker:
            self.play(Write(t1))
            self.wait_until_bookmark('line1')
            self.play(TransformFromCopy(t1[0], t2[0]))
            self.wait_until_bookmark('line2')
            self.play(TransformFromCopy(t1[1], t2[1]))
            self.play(TransformFromCopy(t2[0], t3[0]))
            self.wait_until_bookmark('line3')
            self.play(TransformFromCopy(t2[1], t3[1]))
            self.play(Write(t3[2]))
            self.clear()
            self.play(Write(equation1))
        # Setup axes without numbers
        axes = Axes(
            x_range=[0, 5, 1],  # time range: 0 to 5
            y_range=[0, 10, 2],  # velocity range: 0 to 10
            axis_config={"color": BLUE},
            x_axis_config={"include_ticks": False},  # no ticks on x-axis
            y_axis_config={"include_ticks": False},  # no ticks on y-axis
        )   
    
        # Labels for axes
        x_label = axes.get_x_axis_label(Tex("t"))
        y_label = axes.get_y_axis_label(Tex("v"))
    
        # Initial velocity u, final velocity v, and time t
        u = 2  # initial velocity
        v = 8  # final velocity
        t_final = 4  # final time
    
        # Create a line from (0, u) to (t, v) using the Line object
        vt_line = Line(
            start=axes.c2p(0, u), 
            end=axes.c2p(t_final, v), 
            color=YELLOW
        )
    
    # Create points at (0, u) and (t, v) with labels
        point_u = Dot(axes.c2p(0, u), color=RED)
        point_v = Dot(axes.c2p(t_final, v), color=RED)
    
        u_label = MathTex("u").next_to(point_u, LEFT)
        v_label = MathTex("v").next_to(point_v, RIGHT)
    
    # Gradient label: a = (v - u) / t
        gradient = MathTex(r"a = \frac{v - u}{t}").set_color(GREEN)
        gradient.align_to(vt_line, LEFT)
    
    # Create the shaded area under the graph (as a Polygon)
    # The vertices of the polygon are the points (0, u), (t, v), (t, 0), and (0, 0)
        vt_area = Polygon(
            axes.c2p(0, 0),        # (0, 0)
            axes.c2p(0, u),        # (0, u)
            axes.c2p(t_final, v),  # (t, v)
            axes.c2p(t_final, 0),  # (t, 0)
            color=BLUE, fill_opacity=0.3, stroke_width=0
        )
    # Label for the shaded area
    
    
    
        area_label = Tex(r"$x=$", r"$\frac{v+u}{2} t$",).move_to(axes.c2p(t_final / 2, (u + v) / 4)).set_color(WHITE)
        u_label1 = Text("a")
        v_label1 = Text("b")
        x_label1 = Text("h")
        x_label1.next_to(Line(axes.c2p(0, 0), axes.c2p(t_final, 0)), DOWN)
    # Animations
        with self.voiceover(
            text="""We can also derive equation one using a graph. If we plot velocity against time, we can see that the gradient of the line is equal to acceleration.
            <bookmark mark='line1'/>
            If we label the initial velocity u and the final velocity v, we can see that the gradient a is equal to v minus u over t.
            <bookmark mark='line2'/>
            If we rearrange this equation to make v the subject, we get v equals u plus a t, which is our first equation again.
            <bookmark mark='line3'/>
            Now, if we look at the area under the graph, we can see that this represents displacement, x.
            <bookmark mark='line4'/>
            This area is a trapezium, so we can use the formula for the area of a trapezium to find x. This gives us our 2nd equation.
            <bookmark mark='line5'/>
            """
        ) as tracker:
            self.play(Create(axes), Write(x_label), Write(y_label))
            self.play(Create(vt_line))
            self.wait_until_bookmark('line1')
            self.play(FadeIn(point_u, point_v), Write(u_label), Write(v_label))
            self.wait_until_bookmark('line2')
    
    # Show gradient a = (v - u) / t
        
            self.play(Write(gradient))
            trapezium_equation2 = Tex(r"$Area = \frac{a+b}{2}h$")
            trapezium_equation2.next_to(area_label, RIGHT)
            self.wait_until_bookmark('line3')
            # Animate shading of the area under the graph and label it as x
            self.play(FadeIn(vt_area))
            self.play(Write(area_label[0]))
            self.wait_until_bookmark('line4')
            self.wait(0.5)
            self.play(vt_area.animate.set_stroke(color=WHITE, width=4))
            self.wait(0.5)
            self.play(Write(trapezium_equation2))
            self.wait(1)
            u_label1.next_to(Line(axes.c2p(0, 0), axes.c2p(0, u)), LEFT)
            v_label1.next_to(Line(axes.c2p(t_final, 0), axes.c2p(t_final, v)), RIGHT)
            self.play(Write(u_label1))
            self.play(Write(v_label1))
            self.play(Write(x_label1))
            self.wait(0.5)
            self.play(Write(area_label[1]))
            self.wait_until_bookmark('line5')
            self.wait(3)
            self.clear()
        t4 = Tex(r"$v=u+at$", r"$\ \ (1)$", font_size=72)
        t5 = Tex(r"$x=\frac{u+v}{2}t$", r"$\ \ (2)$", font_size=72)
        t6 = Tex(r"$t=$", r"$\frac{v-u}{a}$", font_size=72)
        t7 = Tex(r"$t=$", r"$\frac{v+u}{2x}$", font_size=72)
        t8 = Tex(r"$\frac{v-u}{a}$", r"$=$", r"$\frac{v+u}{2x}$", font_size=72)
        h = VGroup(t4, t6, t5, t7, t8).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        with self.voiceover("""
            Now, we can derive the 3rd, 4th and 5th equations using equations 1 and 2. First we make t the subject of both equations.
            <bookmark mark='line1'/>
            Then we set the two equations equal to each other.
            <bookmark mark='line2'/>
            From here, we first bring like terms together and then factorise the left hand side.
            Finally, we rearrange to get our 3rd equation.
            v squared equals u squared plus 2 a x.
            <bookmark mark='line3'/>
            So now we have 3 equations. One for v in terms of u, a and t. One for x in terms of u, v and t.
            And one for v squared in terms of u, a and x.
            <bookmark mark='line4'/>
            """) as tracker:             
            self.play(Write(t4))
            self.play(TransformFromCopy(t4, t6))
            self.play(Write(t5))
            self.play(TransformFromCopy(t5, t7))
            self.wait_until_bookmark('line1')
            self.play(Write(t8))
            self.wait_until_bookmark('line2')
            self.wait(2)
            self.clear()
            t9 = Tex(r"$\frac{v-u}{a}$", r"$=$", r"$\frac{v+u}{2x}$", font_size=72)
            t10 = Tex(r"$(v+u)(v-u)$", r"$=$", r"$2ax$", font_size=72)
            t11 = Tex(r"$v^2-u^2$", r"$=$", r"$2ax$", font_size=72)
            t12 = Tex(r"$v^2$", r"$=$", r"$u^2+2ax$", r"\ \ (3)", font_size=72)
            j = VGroup(t9, t10, t11, t12).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            self.play(Write(t9))
            self.play(TransformFromCopy(t9, t10))
            self.wait(0.5)
            self.play(TransformFromCopy(t10, t11))
            self.wait(0.5)
            self.play(TransformFromCopy(t11, t12))
            self.wait_until_bookmark ('line3')
            self.wait(3)
            self.clear()
            k = VGroup(t4, t5, t12).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            self.play(Write(k))
            self.wait(3)
            self.play(k.animate.to_edge(UP))
            self.wait_until_bookmark('line4')
            # Remove t12 from the group
            self.play(FadeOut(t12))
            self.wait(0.5)
        t13 = Tex(r"$v$", r"$=$", r"$\frac{2x}{t}-u$", font_size=72)
        t14 = Tex(r"$\frac{2x}{t}-u$", r"$=$", r"$u+at$", font_size=72)
        t15 = Tex(r"$2x$", r"$=$", r"$2ut+at^2$", font_size=72)
        t16 = Tex(r"$x$", r"$=$", r"$ut+\frac{1}{2}at^2$", r"\ \ (4)", font_size=72)
        t17 = Tex(r"$x$", r"$=$", r"$vt-\frac{1}{2}at^2$", r"\ \ (5)", font_size=72)
        l = VGroup(t13, t14, t15, t16, t17).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        l.next_to(t5, DOWN)
        l.shift(RIGHT * 0.5)
        with self.voiceover("""
            Next, rearrange equation 2 to make v the subject.
            <bookmark mark='line1'/>
            Then we bring all terms to one side.
            <bookmark mark='line2'/>
            Next, we multiply both sides by t and then rearrange to make x the subject.
            This gives us our 4th equation, x equals u t plus one half a t squared.
            <bookmark mark='line3'/>
            Finally, we can derive our 5th equation by making u the subject of equation one and completing the same substitution from before.
            <bookmark mark='line4'/>      
            """) as tracker:
            self.play(TransformFromCopy(t5, t13))
            self.wait(0.5)
            self.wait_until_bookmark('line1')
            self.play(TransformFromCopy(t13, t14))
            self.wait(0.5)
            self.wait_until_bookmark('line2')
            self.play(TransformFromCopy(t14, t15))
            self.wait(0.5)
            self.wait_until_bookmark('line3')
            self.play(TransformFromCopy(t15, t16))
            self.wait(0.5)
            self.play(TransformFromCopy(t16, t17))
            self.wait_until_bookmark('line4')
            self.wait(2)
            self.clear()
        m = VGroup(t4, t5, t12, t16, t17).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        with self.voiceover("""
            We now have all 5 equations. To summarise:
            Equation 1, v equals u plus a t.
            Equation 2, x equals u plus v over 2 times t.
            Equation 3, v squared equals u squared plus 2 a x.
            Equation 4, x equals u t plus one half a t squared.
            And equation 5, x equals v t minus one half a t squared.
            <bookmark mark='line1'/>
            But why all 5, this is because each equation has a different variable missing. 
            This means that depending on what values you have, you can choose the most appropriate equation to use.
            Equation 1 has no x, equation 2 has no a, equation 3 has no t, equation 4 has no v and equation 5 has no u.
            When using these equations, first list the quantities you know and want to find, then select the equation that has these in it. Thanks for watching and I hope this helps. 
            <bookmark mark='line2'/>
            """) as tracker:    
            self.play(Write(m))
            self.wait_until_bookmark('line1')
            x1 = Text("x", font_size=72, color=RED)
            u1 = Text("u", font_size=72, color=RED)
            v1 = Text("v", font_size=72, color=RED)
            a = Text("a", font_size=72, color=RED)
            t1 = Text("t", font_size=72, color=RED)
            n = VGroup(x1, a, t1, v1, u1)
            x1.next_to(t4, RIGHT)
            x1.shift(RIGHT * 0.8)
            a.next_to(t5, RIGHT)
            a.shift(RIGHT * 1.2)
            t1.next_to(t12, RIGHT)
            v1.next_to(t16, RIGHT)
            u1.next_to(t17, RIGHT)
            self.play(Write(n))
            self.wait_until_bookmark('line2')
            self.wait(5)