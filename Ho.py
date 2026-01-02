from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os
import numpy as np
# config.pixel_height = 1920
# config.pixel_width = 1080
# config.frame_height = 16.0
# config.frame_width = 9.0
# Check for Azure credentials

class Ho(VoiceoverScene):
    def construct(self):
         # Configure the voiceover service with Azure
        self.set_speech_service(AzureService(
            voice="en-GB-RyanNeural",  # Male British voice
            style="newscast"
        ))
        
        
        with self.voiceover(text="""
            Edwin Hubble was one of the first astronomers to conclude that there were other galaxies than our own. From his observations in the 1920s, 
            he concluded that nearly all galaxies he could observe were moving away from us and from measuring their red shift, that the further a galaxy is away from us,
            the faster it is moving. This led to him deriving Hubble's law. v, the recession velocity = H 0, Hubble's constant multiplied by the distance the galaxy is away from us.
   
        """) as tracker:
            # Hubble constant (proportionality factor)
            H = 0.2
            
            # Create a grid of stars
            num_stars = 200
            stars = VGroup()
            
            # Generate random positions for stars
            np.random.seed(42)
            for _ in range(num_stars):
                # Random position in a circle around origin
                angle = np.random.uniform(0, 2 * PI)
                radius = np.random.uniform(0.5, 4)
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                
                # Create star as a small dot with varying brightness
                brightness = np.random.uniform(0.4, 1.0)
                size = np.random.uniform(0.02, 0.06)
                
                star = Dot(
                    point=[x, y, 0],
                    radius=size,
                    color=interpolate_color(BLUE, WHITE, brightness)
                )
                stars.add(star)
            
            # Add observer at center
            observer = Dot(color=RED, radius=0.08)
            observer_label = Text("Observer", font_size=20, color=RED).next_to(observer, DOWN, buff=0.2)
            
            self.add(stars, observer, observer_label)
            
            # Title and Hubble's law equation
            title = Text("Hubble's Law: Expanding Universe", font_size=32).to_edge(UP)
            equation = MathTex(r"v = H_0 \cdot d", font_size=28).next_to(title, DOWN)
            equation_label = Text("(velocity = Hubble constant × distance)", font_size=18).next_to(equation, DOWN, buff=0.1)
            
            self.play(Write(title), run_time=1)
            self.play(Write(equation), Write(equation_label), run_time=1)
            self.wait(0.5)
            
            # Animation function that expands stars according to Hubble's law
            def update_stars(mob, dt):
                for star in mob:
                    pos = star.get_center()
                    # Distance from observer (origin)
                    distance = np.linalg.norm(pos)
                    
                    # Velocity proportional to distance (Hubble's law)
                    if distance > 0:
                        velocity = H * distance
                        direction = pos / distance
                        # Update position
                        new_pos = pos + velocity * direction * dt
                        star.move_to(new_pos)
                        
                        # Fade out stars that get too far
                        if distance > 6:
                            star.set_opacity(max(0, 1 - (distance - 6) / 2))
            
            stars.add_updater(update_stars)
            
            # Run the expansion
            self.wait(12)
            
            stars.clear_updaters()
            
            # Add final text
            final_text = Text(
                "Distant galaxies recede faster than nearby ones",
                font_size=24,
                color=YELLOW
            ).to_edge(DOWN)
            self.play(FadeIn(final_text))
            self.wait(2)
            
            # Fade out the text
            self.play(FadeOut(final_text), run_time=0.5)
        with self.voiceover(text="""This work also paved the way for the formation of the big bang theory because if you rewind this expansion, all the galaxies appear to compress to a single point.""") as tracker:
            # Add new text about reversing time
            reverse_text = Text(
                "Reversing time: Back to the Big Bang",
                font_size=24,
                color=YELLOW
            ).to_edge(DOWN)
            self.play(FadeIn(reverse_text))
            self.wait(1)
            
            # Restore opacity to all stars
            for star in stars:
                star.set_opacity(1)
            
            # Animate all stars moving back to the center
            animations = []
            for star in stars:
                animations.append(star.animate.move_to(ORIGIN).set_opacity(0.5))
            
            self.play(*animations, run_time=3, rate_func=smooth)
            
            # Final message
            self.play(FadeOut(reverse_text))
            big_bang_text = Text(
                "The Big Bang: All matter in one point",
                font_size=28,
                color=RED
            ).to_edge(DOWN)
            self.play(FadeIn(big_bang_text))
            self.wait(5)
        
        # Fade out text and observer, but keep stars
        self.play(
            FadeOut(title),
            FadeOut(equation),
            FadeOut(equation_label),
            FadeOut(observer),
            FadeOut(observer_label),
            FadeOut(big_bang_text)
        )
        
        # Redistribute stars across the screen for background effect
        # Make them dimmer and smaller so they don't interfere with equations
        for star in stars:
            # Random position across entire screen
            angle = np.random.uniform(0, 2 * PI)
            radius = np.random.uniform(1, 5)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            star.set_opacity(0.3)  # Dim them down
            star.scale(0.7)  # Make them smaller
        
        # Animate stars spreading out to new positions
        star_animations = [star.animate.move_to([
            np.random.uniform(-7, 7),
            np.random.uniform(-4, 4),
            0
        ]) for star in stars]
        self.play(*star_animations, run_time=2)
        
        # Add subtle outward expansion updater for background stars
        def subtle_expansion(mob, dt):
            for star in mob:
                pos = star.get_center()
                distance = np.linalg.norm(pos)
                
                if distance > 0:
                    # Very slow expansion rate
                    velocity = 0.05 * distance
                    direction = pos / distance
                    new_pos = pos + velocity * direction * dt
                    star.move_to(new_pos)
                    
                    # Fade out and respawn stars that get too far
                    if distance > 8:
                        # Reset star to a position near center
                        angle = np.random.uniform(0, 2 * PI)
                        radius = np.random.uniform(0.5, 2)
                        new_x = radius * np.cos(angle)
                        new_y = radius * np.sin(angle)
                        star.move_to([new_x, new_y, 0])
                        star.set_opacity(0.3)
        
        stars.add_updater(subtle_expansion)
        
        with self.voiceover(text="""
            If we look at Hubble's law it has the form of speed = constant times distance. <bookmark mark='hubble'/>
            From unit analysis, this constant must have the form of 1 over time. So if we assume these galaxies have been moving since the beginning of the universe, then this time is how long since the big bang. <bookmark mark='time'/>
            There is currently debate about the exact value of Hubble's constant, <bookmark mark='values'/> it could be as low as 67 kilometres per second per Megaparsec, or as high as 74. 
            Whilst using this value of H0 to estimate the age of the universe is on A level specifications, converting it from these units to per second is not.   
            So we will not go through that here, however <bookmark mark ='conversion'/> our 67 value becomes 2.17 times 10 to the negative 18 and 74 becomes  2.37 times 10 to the negative 18 
            As both of these have units of per second. If we find the inverse of them we can calculate the age of the universe in seconds. <bookmark mark="ageseconds"/> 
            This gives us the age of the universe to be between 4.6 times 10 to the 17 seconds and 4.2 times ten to the 17 seconds.
            Converting this to years, this gives an esitmate for the age of the universe to be <bookmark mark="ageyears"/> between 14.6 and 13.2 billion years old.
            The discrepancy between these figures is a matter for cutting edge research currently, could it be that one method is flawed or is it dark matter and energy messing up our results. Thanks for watching and hopefully this video helps with your exams.
            """)as tracker:
            Ho_low = 67
            Ho_High = 74
            Ho_convert = 3.24e-20
            Units = MathTex(r"km s^{-1}Mpc^{-1}",r"s^{-1}")
            Title_age_of_universe = Text("Estimating the Age of the Universe", font_size=32).to_edge(UP)
            # Re-create equation for this section
            equation = MathTex(r"v = H_0 \cdot d", font_size=28).next_to(Title_age_of_universe, DOWN)
            equation_label = Text("(velocity = Hubble constant × distance)", font_size=18).next_to(equation, DOWN, buff=0.1)
            
            self.play(Write(Title_age_of_universe))
            self.play(Write(equation), Write(equation_label))
            self.wait_until_bookmark("hubble")
            speed_equation = MathTex(r"s=\frac {d}{t}", font_size=28).next_to(equation_label, DOWN, buff = 0.25)
            self.play(Write(speed_equation))
            Ho_equation = MathTex(r"H_0= \frac{1}{time}", font_size=28).next_to(speed_equation, DOWN, buff = 0.25)
            self.play(Write(Ho_equation))
            age_of_universe = MathTex(r"time = \frac{1}{H_0}", font_size=28).next_to(Ho_equation, DOWN, buff = 0.25)
            self.play(Write(age_of_universe))
            self.wait_until_bookmark('time')
            self.wait(2)
            Ho_low_text = MathTex(r"H_0\ lowest =", {Ho_low},r" km s^{-1}Mpc^{-1}", font_size=28)
            Ho_High_text = MathTex(r"H_0\ highest =", {Ho_High},r" km s^{-1}Mpc^{-1}", font_size=28)
            Ho_group = VGroup(Ho_low_text,Ho_High_text).arrange(RIGHT, buff=1).next_to(age_of_universe,DOWN,buff=0.25)
            self.wait_until_bookmark('values')
            self.play(Write(Ho_group))
            Ho_low_text_convert = MathTex(r"H_0\ lowest =", {round(Ho_low*Ho_convert*1e18,2)},r" \times 10^{-18} s^{-1}", font_size=28)
            Ho_High_text_convert = MathTex(r"H_0\ highest=", {round(Ho_High*Ho_convert*1e18,2)},r" \times 10^{-18} s^{-1}", font_size=28)
            Ho_group_1 = VGroup(Ho_low_text_convert, Ho_High_text_convert).arrange(RIGHT, buff=1).next_to(age_of_universe,DOWN,buff=0.25)
            self.wait_until_bookmark('conversion')
            self.play(Transform(Ho_low_text,Ho_low_text_convert),Transform(Ho_High_text, Ho_High_text_convert))
            oldest_universe_seconds = MathTex(r"Oldest\ Age =", {round(1/(round(Ho_low*Ho_convert*1e18,2)/1e18)/1e17,2)},r"\times 10^{17} s", font_size=28)
            newest_universe_seconds = MathTex(r"Youngest\ Age =",  {round(1/(round(Ho_High*Ho_convert*1e18,2)/1e18)/1e17,2)},r"\times 10^{17} s", font_size=28)
            age_seconds= VGroup(oldest_universe_seconds, newest_universe_seconds).arrange(RIGHT, buff=1).next_to(Ho_group_1,DOWN,buff=0.25)
            self.wait_until_bookmark('ageseconds')
            self.play(Write(age_seconds))
            oldest_universe_years = MathTex(r"Oldest\ Age =",{round(round(1/(round(Ho_low*Ho_convert*1e18,2)/1e18)/1e17,2)*1e17/(365*86400*1e9),2)} ,r"\ billions\ of \ years", font_size=28)
            newest_universe_years = MathTex(r"Youngest\ Age =",{round(round(1/(round(Ho_High*Ho_convert*1e18,2)/1e18)/1e17,2)*1e17/(365*86400*1e9),2)},r"\ billion\ of \ years", font_size=28)
            age_years= VGroup(oldest_universe_years, newest_universe_years).arrange(RIGHT, buff=1).next_to(Ho_group_1,DOWN,buff=0.25)
            self.wait_until_bookmark('ageyears')
            self.play(Transform(age_seconds,age_years))
            self.wait(5)
        
        # Final fade out includes stars
        self.play(*[FadeOut(mob) for mob in self.mobjects])