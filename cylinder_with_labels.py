from manim import *

class Cylinder2DView(Scene):
    def construct(self):
        # Create the 2D representation of a cylinder
        # Circle for the left face
        circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)
        
        # Rectangle for the body
        rectangle = Rectangle(
            height=2,  # height should be 2 * radius to match circle
            width=3,
            color=BLUE,
            fill_opacity=0.3
        )
        
        # Create ellipse for the right end (to give 3D effect)
        right_end = Ellipse(
            width=1,  # slightly narrower to give perspective
            height=2,
            color=BLUE,
            fill_opacity=0.2
        )
        
        # Position shapes
        rectangle.move_to(ORIGIN)
        circle.move_to(rectangle.get_left())
        right_end.move_to(rectangle.get_right())
        
        # Create the shape (order matters for layering)
        cylinder_2d = VGroup(right_end, rectangle, circle)
        
        # Add the labels
        area_label = MathTex("A").next_to(circle, LEFT)
        length_label = MathTex("l").next_to(rectangle, UP)
        
        # Create arrows
        area_arrow = Arrow(
            start=area_label.get_right(),
            end=circle.get_left(),
            color=WHITE,
            buff=0.1
        )
        
        length_arrow = DoubleArrow(
            start=circle.get_center(),
            end=right_end.get_center(),
            color=WHITE,
            buff=0.1
        ).next_to(rectangle, UP, buff=0.2)
        
        # Animation sequence
        self.play(
            FadeIn(rectangle),
            FadeIn(right_end),
            FadeIn(circle)
        )
        self.play(
            Write(area_label),
            Create(area_arrow)
        )
        self.play(
            Write(length_label),
            Create(length_arrow)
        )
        
        self.wait(2)