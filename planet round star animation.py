            a = 2  # semi-major axis
            b = 1.25  # semi-minor axis
            ellipse3 = Ellipse(width=2*a, height=2*b, color=WHITE)
            ellipse3.shift(DOWN * 1.2)

            # Sun position at left focus
            sun_pos = ellipse3.get_center() + LEFT * c
            sun2 = Dot(sun_pos, color=YELLOW, radius=0.15)
            sun2_label = Text("Sun", font_size=18, color=YELLOW)
            sun2_label.next_to(sun2, DOWN, buff=0.15)

            self.play(Create(ellipse3), FadeIn(sun2), Write(sun2_label))
            self.wait()
            start_angle = 5
            # Create planet
            planet = Dot(ellipse3.point_at_angle(start_angle), color=BLUE, radius=0.1)
            
            # Add semi-major axis line and label
            center = ellipse3.get_center()
            right_vertex = center + RIGHT * 2  # semi-major axis length is half of width (4/2 = 2)
            a_line = Line(center, right_vertex, color=RED)
            a_label = MathTex("a", color=RED, font_size=24)
            a_label.next_to(a_line, UP, buff=0.1)

            # Add distance line from sun to planet and label
            r_line = Line(sun_pos, planet.get_center(), color=GREEN)
            r_label = MathTex("r", color=GREEN, font_size=24)
            r_label.move_to(r_line.get_center() + UP * 0.2)

            # Add updater to make r_line and r_label follow the planet
            def update_r_line(line):
                line.put_start_and_end_on(sun_pos, planet.get_center())

            def update_r_label(label):
                label.move_to(r_line.get_center() + UP * 0.2)

            r_line.add_updater(update_r_line)
            r_label.add_updater(update_r_label)

            self.play(
                FadeIn(planet),
                Create(a_line), Write(a_label),
                Create(r_line), Write(r_label)
            )

            # Create a partial path starting from the planet's current position
            # Get the starting angle (5 degrees) and create a path from there
            def ellipse_func(t):
                angle = start_angle + t * 2 * PI  # Start from start_angle
                return np.array([
                    a * np.cos(angle),
                    b * np.sin(angle),
                0
            ])
            path = ParametricFunction(
            ellipse_func,
            t_range=[0, 1],
            color=WHITE
        )
            path.shift(DOWN * 1.2)
            self.play(MoveAlongPath(planet, path), run_time=5, rate_func=linear)

            # Remove updaters when done
            r_line.remove_updater(update_r_line)
            r_label.remove_updater(update_r_label)