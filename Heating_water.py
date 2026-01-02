from manim import *
import random
import math


class Intro(Scene):
    def construct(self):
        

        # Create 4x4 grid of small blue circles inside the box
        rows, cols = 4, 4
        side = 3
        # Compute radius so circles almost touch (small gap) and are centered inside the box
        gap = 0.04
        margin = 0.2
        r = 0.1
        # spacing between centers (diameter + gap)
        spacing = 2 * r + gap

        circles = VGroup()

        # Calculate the total width of the grid
        grid_width = (cols - 1) * spacing + 2 * r

        # Center the grid horizontally, position at bottom vertically
        x0 = -grid_width / 2 + r
        # Start from the bottom of the box plus radius (so circle sits on bottom edge)
        y0 = -side / 2 + r

        for i in range(rows):
            for j in range(cols):
                cx = x0 + j * spacing
                cy = y0 + i * spacing
                c = Circle(radius=r, color=BLUE, fill_opacity=0.8)
                c.move_to(np.array([cx, cy, 0]))
                # store initial center and random phase for gentle vibration
                c.initial_center = np.array([cx, cy, 0])
                c.phase_x = random.uniform(0, 2 * math.pi)
                c.phase_y = random.uniform(0, 2 * math.pi)
                c.t = 0.0

                # Much smaller amplitude for gentle vibration
                amp_x = 0.03  # Small vibration
                amp_y = 0.03

                freq = random.uniform(0.5, 1.0)  # Slower frequency

                def make_updater(circle, amp_x=amp_x, amp_y=amp_y, freq=freq):
                    def updater(m, dt):
                        circle.t += dt
                        dx = amp_x * math.sin(2 * math.pi * freq * circle.t + circle.phase_x)
                        dy = amp_y * math.sin(2 * math.pi * freq * circle.t + circle.phase_y)
                        m.move_to(circle.initial_center + np.array([dx, dy, 0]))
                    return updater

                c.add_updater(make_updater(c))
                circles.add(c)
        box = Square(side_length=side)
        # Add box and circles together
        self.add(box, circles)
        self.wait(60)

class solid_heating(Scene):
    def construct(self):
        # Create 4x4 grid of small blue circles inside the box
        rows, cols = 4, 4
        side = 3
        # Compute radius so circles almost touch (small gap) and are centered inside the box
        gap = 0.04
        margin = 0.2
        r = 0.1
        # spacing between centers (diameter + gap)
        spacing = 2 * r + gap

        circles = VGroup()

        # Calculate the total width of the grid
        grid_width = (cols - 1) * spacing + 2 * r

        # Center the grid horizontally, position at bottom vertically
        x0 = -grid_width / 2 + r
        # Start from the bottom of the box plus radius (so circle sits on bottom edge)
        y0 = -side / 2 + r

        # Box bounds
        left_bound = -side / 2 + r
        right_bound = side / 2 - r
        bottom_bound = -side / 2 + r
        top_bound = side / 2 - r

        for i in range(rows):
            for j in range(cols):
                cx = x0 + j * spacing
                cy = y0 + i * spacing
                c = Circle(radius=r, color=BLUE, fill_opacity=0.8)
                c.move_to(np.array([cx, cy, 0]))
                # store initial center and random phase for gentle vibration
                c.initial_center = np.array([cx, cy, 0])
                c.phase_x = random.uniform(0, 2 * math.pi)
                c.phase_y = random.uniform(0, 2 * math.pi)
                c.t = 0.0
                c.phase_t = 0.0  # Separate time tracker for phase

                # Initial and final parameters for heating
                initial_amp = 0.01  # Very small initial vibration
                final_amp = 0.08    # Still small but noticeable final vibration
                initial_freq = 0.3  # Slow initial frequency
                final_freq = 1.0    # Slower final frequency
                heating_duration = 20.0  # 20 seconds to heat up

                def make_updater(circle, init_amp=initial_amp, fin_amp=final_amp, 
                               init_freq=initial_freq, fin_freq=final_freq, 
                               heat_time=heating_duration):
                    def updater(m, dt):
                        circle.t += dt
                        
                        # Calculate heating progress (0 to 1 over heating_duration)
                        progress = min(circle.t / heat_time, 1.0)
                        
                        # Linearly interpolate amplitude and frequency
                        current_amp = init_amp + (fin_amp - init_amp) * progress
                        current_freq = init_freq + (fin_freq - init_freq) * progress
                        
                        # Update phase time based on current frequency
                        circle.phase_t += dt * current_freq
                        
                        dx = current_amp * math.sin(2 * math.pi * circle.phase_t + circle.phase_x)
                        dy = current_amp * math.sin(2 * math.pi * circle.phase_t + circle.phase_y)
                        
                        # Calculate new position
                        new_x = circle.initial_center[0] + dx
                        new_y = circle.initial_center[1] + dy
                        
                        # Clamp to box bounds
                        new_x = max(left_bound, min(right_bound, new_x))
                        new_y = max(bottom_bound, min(top_bound, new_y))
                        
                        m.move_to(np.array([new_x, new_y, 0]))
                    return updater

                c.add_updater(make_updater(c))
                circles.add(c)
                
        box = Square(side_length=side)
        # Add box and circles together
        self.add(box, circles)
        self.wait(25)

class Melting(Scene):
    def construct(self):
        # Create 4x4 grid of small blue circles inside the box
        rows, cols = 4, 4
        side = 3
        gap = 0.04
        margin = 0.2
        r = 0.1
        spacing = 2 * r + gap

        circles = VGroup()

        # Calculate the total width of the grid
        grid_width = (cols - 1) * spacing + 2 * r

        # Center the grid horizontally, position at bottom vertically
        x0 = -grid_width / 2 + r
        y0 = -side / 2 + r

        # Box bounds
        left_bound = -side / 2 + r
        right_bound = side / 2 - r
        bottom_bound = -side / 2 + r
        top_bound = side / 2 - r

        for i in range(rows):
            for j in range(cols):
                cx = x0 + j * spacing
                cy = y0 + i * spacing
                c = Circle(radius=r, color=BLUE, fill_opacity=0.8)
                c.move_to(np.array([cx, cy, 0]))
                
                # Store initial position from solid state
                c.initial_center = np.array([cx, cy, 0])
                c.current_center = np.array([cx, cy, 0])  # Track current center as it drifts
                
                # Random target position in liquid - spread across full width of box
                # Use the full box width minus margin for radius
                target_x = random.uniform(left_bound + 0.05, right_bound - 0.05)
                # Keep particles in bottom 2-3 layers
                target_y = random.uniform(bottom_bound, bottom_bound + spacing * 2.5)
                c.target_center = np.array([target_x, target_y, 0])
                
                c.phase_x = random.uniform(0, 2 * math.pi)
                c.phase_y = random.uniform(0, 2 * math.pi)
                c.t = 0.0
                c.phase_t = 0.0
                
                # Start with solid parameters (end state from previous scene)
                start_amp = 0.08
                liquid_amp = 0.12  # Slightly larger vibrations in liquid
                start_freq = 1.0
                liquid_freq = 1.5  # Faster vibrations in liquid
                
                melting_duration = 15.0  # 15 seconds to fully melt

                def make_updater(circle, s_amp=start_amp, l_amp=liquid_amp,
                               s_freq=start_freq, l_freq=liquid_freq,
                               melt_time=melting_duration):
                    def updater(m, dt):
                        circle.t += dt
                        
                        # Calculate melting progress (0 to 1)
                        progress = min(circle.t / melt_time, 1.0)
                        
                        # Interpolate vibration parameters
                        current_amp = s_amp + (l_amp - s_amp) * progress
                        current_freq = s_freq + (l_freq - s_freq) * progress
                        
                        # Update phase time
                        circle.phase_t += dt * current_freq
                        
                        # Gradually drift from initial position to target position
                        circle.current_center = (
                            circle.initial_center * (1 - progress) + 
                            circle.target_center * progress
                        )
                        
                        # Calculate vibration offset
                        dx = current_amp * math.sin(2 * math.pi * circle.phase_t + circle.phase_x)
                        dy = current_amp * math.sin(2 * math.pi * circle.phase_t + circle.phase_y)
                        
                        # Calculate new position
                        new_x = circle.current_center[0] + dx
                        new_y = circle.current_center[1] + dy
                        
                        # Clamp to box bounds
                        new_x = max(left_bound, min(right_bound, new_x))
                        new_y = max(bottom_bound, min(top_bound, new_y))
                        
                        m.move_to(np.array([new_x, new_y, 0]))
                    return updater

                c.add_updater(make_updater(c))
                circles.add(c)
                
        box = Square(side_length=side)
        self.add(box, circles)
        self.wait(20)  # 15s melting + 5s settled

class Heating_water(Scene):
    def construct(self):
        # Create 4x4 grid of small blue circles inside the box
        rows, cols = 4, 4
        side = 3
        gap = 0.04
        margin = 0.2
        r = 0.1
        spacing = 2 * r + gap

        circles = VGroup()

        # Box bounds
        left_bound = -side / 2 + r
        right_bound = side / 2 - r
        bottom_bound = -side / 2 + r
        top_bound = side / 2 - r

        # Create particles in liquid state (random positions at bottom)
        for i in range(rows * cols):
            # Random position spread across bottom of box
            cx = random.uniform(left_bound + 0.05, right_bound - 0.05)
            cy = random.uniform(bottom_bound, bottom_bound + spacing * 2.5)
            
            c = Circle(radius=r, color=BLUE, fill_opacity=0.8)
            c.move_to(np.array([cx, cy, 0]))
            
            # Store center as it drifts
            c.current_center = np.array([cx, cy, 0])
            
            c.phase_x = random.uniform(0, 2 * math.pi)
            c.phase_y = random.uniform(0, 2 * math.pi)
            c.t = 0.0
            c.phase_t = 0.0
            
            # Start with liquid parameters (end state from previous scene)
            start_amp = 0.12
            hot_liquid_amp = 0.18  # More energetic movement when heated
            start_freq = 1.5
            hot_liquid_freq = 2.5  # Much faster vibrations when hot
            
            heating_duration = 750.0  # 12.5 minutes = 750 seconds

            def make_updater(circle, s_amp=start_amp, h_amp=hot_liquid_amp,
                           s_freq=start_freq, h_freq=hot_liquid_freq,
                           heat_time=heating_duration):
                def updater(m, dt):
                    circle.t += dt
                    
                    # Calculate heating progress (0 to 1)
                    progress = min(circle.t / heat_time, 1.0)
                    
                    # Interpolate vibration parameters
                    current_amp = s_amp + (h_amp - s_amp) * progress
                    current_freq = s_freq + (h_freq - s_freq) * progress
                    
                    # Update phase time
                    circle.phase_t += dt * current_freq
                    
                    # Add slight drift for liquid movement
                    drift_speed = 0.05 * progress  # Increases with temperature
                    drift_x = drift_speed * math.sin(0.3 * circle.t + circle.phase_x * 0.5) * dt
                    drift_y = drift_speed * math.sin(0.4 * circle.t + circle.phase_y * 0.5) * dt
                    
                    circle.current_center[0] += drift_x
                    circle.current_center[1] += drift_y
                    
                    # Keep center within bounds (with some margin)
                    circle.current_center[0] = max(left_bound + 0.1, min(right_bound - 0.1, circle.current_center[0]))
                    circle.current_center[1] = max(bottom_bound, min(bottom_bound + spacing * 3, circle.current_center[1]))
                    
                    # Calculate vibration offset
                    dx = current_amp * math.sin(2 * math.pi * circle.phase_t + circle.phase_x)
                    dy = current_amp * math.sin(2 * math.pi * circle.phase_t + circle.phase_y)
                    
                    # Calculate new position
                    new_x = circle.current_center[0] + dx
                    new_y = circle.current_center[1] + dy
                    
                    # Clamp to box bounds
                    new_x = max(left_bound, min(right_bound, new_x))
                    new_y = max(bottom_bound, min(top_bound, new_y))
                    
                    m.move_to(np.array([new_x, new_y, 0]))
                return updater

            c.add_updater(make_updater(c))
            circles.add(c)
            
        box = Square(side_length=side)
        self.add(box, circles)
        self.wait(110)  # 750s (12.5 min) heating + 10s at hot temperature

class Boiling(Scene):
    def construct(self):
        # Create 4x4 grid of small blue circles inside the box
        rows, cols = 4, 4
        side = 3
        gap = 0.04
        margin = 0.2
        r = 0.1
        spacing = 2 * r + gap

        circles = VGroup()

        # Box bounds
        left_bound = -side / 2 + r
        right_bound = side / 2 - r
        bottom_bound = -side / 2 + r
        top_bound = side / 2 - r
        
        # Transition height (1/3 up the box)
        transition_height = -side / 2 + side / 3

        # Create particles in hot liquid state (random positions at bottom)
        for i in range(rows * cols):
            # Random position spread across bottom of box
            cx = random.uniform(left_bound + 0.05, right_bound - 0.05)
            cy = random.uniform(bottom_bound, bottom_bound + spacing * 2.5)
            
            c = Circle(radius=r, color=BLUE, fill_opacity=0.8)
            c.move_to(np.array([cx, cy, 0]))
            
            # Store center position
            c.current_pos = np.array([cx, cy, 0])
            c.is_gas = False  # Track whether particle has transitioned to gas
            
            # Random velocity for gas phase - much faster
            c.final_speed = random.uniform(1.5, 2.5)  # Increased from 0.5-1.2
            c.final_angle = random.uniform(0, 2 * math.pi)
            c.vx = 0.0
            c.vy = 0.0
            
            c.phase_x = random.uniform(0, 2 * math.pi)
            c.phase_y = random.uniform(0, 2 * math.pi)
            c.t = 0.0
            c.phase_t = 0.0
            
            # Liquid parameters
            liquid_amp = 0.18
            liquid_freq = 2.5
            
            # Random time when this particle starts transitioning (stagger the boiling)
            c.transition_start = random.uniform(5.0, 20.0)
            c.transition_duration = 3.0  # Takes 3 seconds to transition

            def make_updater(circle, l_amp=liquid_amp, l_freq=liquid_freq,
                           trans_height=transition_height):
                def updater(m, dt):
                    circle.t += dt
                    
                    # Check if particle should transition to gas
                    if not circle.is_gas:
                        # LIQUID PHASE - vibrating at bottom
                        
                        # Start building up velocity after transition_start time
                        if circle.t > circle.transition_start:
                            trans_progress = min((circle.t - circle.transition_start) / circle.transition_duration, 1.0)
                            circle.vx = circle.final_speed * math.cos(circle.final_angle) * trans_progress
                            circle.vy = circle.final_speed * math.sin(circle.final_angle) * trans_progress
                            
                            # Update position with increasing velocity
                            circle.current_pos[0] += circle.vx * dt
                            circle.current_pos[1] += circle.vy * dt
                        
                        # Update vibration phase
                        circle.phase_t += dt * l_freq
                        dx = l_amp * math.sin(2 * math.pi * circle.phase_t + circle.phase_x)
                        dy = l_amp * math.sin(2 * math.pi * circle.phase_t + circle.phase_y)
                        
                        # Check if particle has crossed transition height - becomes gas
                        if circle.current_pos[1] > trans_height:
                            circle.is_gas = True
                            # Set full gas velocity
                            circle.vx = circle.final_speed * math.cos(circle.final_angle)
                            circle.vy = circle.final_speed * math.sin(circle.final_angle)
                        
                        # Apply position with vibration
                        final_x = circle.current_pos[0] + dx
                        final_y = circle.current_pos[1] + dy
                        
                        # Clamp to bounds even in liquid phase
                        final_x = max(left_bound, min(right_bound, final_x))
                        final_y = max(bottom_bound, min(top_bound, final_y))
                        
                    else:
                        # GAS PHASE - straight line motion with bouncing
                        
                        # Update position based on velocity
                        circle.current_pos[0] += circle.vx * dt
                        circle.current_pos[1] += circle.vy * dt
                        
                        # Bounce off walls
                        if circle.current_pos[0] <= left_bound:
                            circle.vx = abs(circle.vx)
                            circle.current_pos[0] = left_bound + 0.01
                        elif circle.current_pos[0] >= right_bound:
                            circle.vx = -abs(circle.vx)
                            circle.current_pos[0] = right_bound - 0.01
                        
                        if circle.current_pos[1] <= bottom_bound:
                            circle.vy = abs(circle.vy)
                            circle.current_pos[1] = bottom_bound + 0.01
                        elif circle.current_pos[1] >= top_bound:
                            circle.vy = -abs(circle.vy)
                            circle.current_pos[1] = top_bound - 0.01
                        
                        # No vibration in gas phase
                        final_x = circle.current_pos[0]
                        final_y = circle.current_pos[1]
                    
                    m.move_to(np.array([final_x, final_y, 0]))
                return updater

            c.add_updater(make_updater(c))
            circles.add(c)
            
        box = Square(side_length=side)
        self.add(box, circles)
        self.wait(30)  # Watch the boiling process

class Steam(Scene):
    def construct(self):
        # Create 4x4 grid of small blue circles inside the box
        rows, cols = 4, 4
        side = 3
        r = 0.1

        circles = VGroup()

        # Box bounds
        left_bound = -side / 2 + r
        right_bound = side / 2 - r
        bottom_bound = -side / 2 + r
        top_bound = side / 2 - r

        # Create particles as gas distributed throughout the box
        for i in range(rows * cols):
            # Random position anywhere in the box
            cx = random.uniform(left_bound + 0.1, right_bound - 0.1)
            cy = random.uniform(bottom_bound + 0.1, top_bound - 0.1)
            
            c = Circle(radius=r, color=BLUE, fill_opacity=0.8)
            c.move_to(np.array([cx, cy, 0]))
            
            # Store current position
            c.current_pos = np.array([cx, cy, 0])
            
            # Starting gas velocity (from end of boiling scene)
            c.initial_speed = random.uniform(1.5, 2.5)
            c.final_speed = random.uniform(3.0, 4.5)  # Much faster when heated
            c.angle = random.uniform(0, 2 * math.pi)
            
            # Set initial velocity
            c.vx = c.initial_speed * math.cos(c.angle)
            c.vy = c.initial_speed * math.sin(c.angle)
            
            c.t = 0.0
            
            heating_duration = 15.0  # 15 seconds to heat the gas

            def make_updater(circle, heat_time=heating_duration):
                def updater(m, dt):
                    circle.t += dt
                    
                    # Calculate heating progress (0 to 1)
                    progress = min(circle.t / heat_time, 1.0)
                    
                    # Interpolate speed
                    current_speed = circle.initial_speed + (circle.final_speed - circle.initial_speed) * progress
                    
                    # Update velocity magnitude while maintaining direction
                    speed_ratio = current_speed / (circle.vx**2 + circle.vy**2)**0.5
                    circle.vx *= speed_ratio
                    circle.vy *= speed_ratio
                    
                    # Update position based on velocity
                    circle.current_pos[0] += circle.vx * dt
                    circle.current_pos[1] += circle.vy * dt
                    
                    # Bounce off walls
                    if circle.current_pos[0] <= left_bound:
                        circle.vx = abs(circle.vx)
                        circle.current_pos[0] = left_bound + 0.01
                    elif circle.current_pos[0] >= right_bound:
                        circle.vx = -abs(circle.vx)
                        circle.current_pos[0] = right_bound - 0.01
                    
                    if circle.current_pos[1] <= bottom_bound:
                        circle.vy = abs(circle.vy)
                        circle.current_pos[1] = bottom_bound + 0.01
                    elif circle.current_pos[1] >= top_bound:
                        circle.vy = -abs(circle.vy)
                        circle.current_pos[1] = top_bound - 0.01
                    
                    m.move_to(np.array([circle.current_pos[0], circle.current_pos[1], 0]))
                return updater

            c.add_updater(make_updater(c))
            circles.add(c)
            
        box = Square(side_length=side)
        self.add(box, circles)
        self.wait(20)  # 15s heating + 5s at maximum temperature