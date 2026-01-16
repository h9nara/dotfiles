#!/usr/bin/env python3
"""Create a fun GIF showing Skills are way cooler than MCPs"""

import sys
sys.path.insert(0, '/Users/han/.claude/skills/slack-gif-creator')

import math
from PIL import Image, ImageDraw, ImageFont
from core.gif_builder import GIFBuilder
from core.frame_composer import create_gradient_background, draw_star
from core.easing import ease_out_elastic, ease_out_bounce

# Settings
WIDTH, HEIGHT = 480, 480
FPS = 15
NUM_FRAMES = 30  # 2 second loop

builder = GIFBuilder(width=WIDTH, height=HEIGHT, fps=FPS)

def draw_sparkle(draw, x, y, size, color, rotation=0):
    """Draw a 4-pointed sparkle/star"""
    points = []
    for i in range(8):
        angle = (i * 45 + rotation) * math.pi / 180
        r = size if i % 2 == 0 else size * 0.3
        px = x + r * math.cos(angle)
        py = y + r * math.sin(angle)
        points.append((px, py))
    draw.polygon(points, fill=color)

def get_rainbow_color(t, saturation=1.0):
    """Get rainbow color based on t (0-1)"""
    hue = t * 360
    # HSV to RGB conversion
    c = saturation
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = 1 - c

    if hue < 60:
        r, g, b = c, x, 0
    elif hue < 120:
        r, g, b = x, c, 0
    elif hue < 180:
        r, g, b = 0, c, x
    elif hue < 240:
        r, g, b = 0, x, c
    elif hue < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return (int((r + m) * 255), int((g + m) * 255), int((b + m) * 255))

# Sparkle positions (will animate)
sparkle_positions = [
    (80, 120), (400, 100), (60, 200), (420, 180),
    (100, 280), (380, 260), (150, 140), (330, 160)
]

for frame_idx in range(NUM_FRAMES):
    t = frame_idx / NUM_FRAMES

    # Create gradient background (cool purple to blue)
    frame = create_gradient_background(WIDTH, HEIGHT, (40, 20, 80), (20, 40, 100))
    draw = ImageDraw.Draw(frame)

    # === SKILLS section (top) - vibrant and animated ===

    # Pulsing/bouncing effect for Skills
    pulse = math.sin(t * 2 * math.pi) * 0.15 + 1.0  # Scale between 0.85 and 1.15
    bounce_y = math.sin(t * 4 * math.pi) * 10  # Bounce up and down

    # Draw glowing background for SKILLS
    glow_color = get_rainbow_color(t)
    glow_size = int(180 * pulse)
    draw.ellipse(
        [WIDTH//2 - glow_size, 120 - glow_size//2 + bounce_y,
         WIDTH//2 + glow_size, 120 + glow_size//2 + bounce_y],
        fill=(glow_color[0]//4, glow_color[1]//4, glow_color[2]//4)
    )

    # Draw "SKILLS" text with rainbow effect
    skills_text = "SKILLS"
    # Use a larger approach - draw each letter
    letter_width = 50
    start_x = WIDTH//2 - (len(skills_text) * letter_width) // 2

    for i, letter in enumerate(skills_text):
        letter_t = (t + i * 0.1) % 1.0
        color = get_rainbow_color(letter_t)
        letter_bounce = math.sin((t * 4 + i * 0.3) * math.pi) * 8

        # Draw letter shadow
        x = start_x + i * letter_width
        y = 100 + letter_bounce + bounce_y

        # Shadow
        draw.text((x + 3, y + 3), letter, fill=(0, 0, 0),
                  font=ImageFont.load_default(size=48))
        # Letter
        draw.text((x, y), letter, fill=color,
                  font=ImageFont.load_default(size=48))

    # Draw animated sparkles around SKILLS
    for i, (sx, sy) in enumerate(sparkle_positions):
        sparkle_t = (t + i * 0.125) % 1.0
        sparkle_size = 8 + math.sin(sparkle_t * 2 * math.pi) * 6
        rotation = (t * 360 + i * 45) % 360
        color = get_rainbow_color((t + i * 0.1) % 1.0)

        # Only draw sparkles in top half
        if sy < HEIGHT // 2:
            draw_sparkle(draw, sx, sy + bounce_y * 0.5, sparkle_size, color, rotation)

    # Draw stars around Skills
    for i in range(4):
        angle = (t * 360 + i * 90) * math.pi / 180
        radius = 160
        star_x = WIDTH//2 + radius * math.cos(angle)
        star_y = 140 + radius * 0.4 * math.sin(angle) + bounce_y
        star_color = get_rainbow_color((t + i * 0.25) % 1.0)
        draw_star(frame, (int(star_x), int(star_y)), 15, star_color, outline_color=(255, 255, 255), outline_width=2)

    # === VS section (middle) ===
    draw.text((WIDTH//2 - 20, HEIGHT//2 - 20), "vs", fill=(100, 100, 120),
              font=ImageFont.load_default(size=32))

    # === MCPs section (bottom) - boring and static ===

    # Gray boring background
    draw.rectangle([100, 320, 380, 400], fill=(50, 50, 55), outline=(60, 60, 65), width=2)

    # Draw "MCPs" in boring gray - completely static
    mcp_text = "MCPs"
    mcp_x = WIDTH//2 - 60
    mcp_y = 340

    # Boring gray color
    boring_gray = (120, 120, 130)
    draw.text((mcp_x, mcp_y), mcp_text, fill=boring_gray,
              font=ImageFont.load_default(size=40))

    # Add "zzz" to show MCPs are sleepy/boring
    zzz_offset = math.sin(t * math.pi) * 3
    draw.text((390, 330 + zzz_offset), "z", fill=(80, 80, 90),
              font=ImageFont.load_default(size=16))
    draw.text((400, 320 + zzz_offset), "z", fill=(90, 90, 100),
              font=ImageFont.load_default(size=20))
    draw.text((415, 305 + zzz_offset), "z", fill=(100, 100, 110),
              font=ImageFont.load_default(size=24))

    # Add dust/cobwebs to MCPs (static dots)
    for dx, dy in [(110, 330), (115, 395), (365, 335), (370, 390)]:
        draw.ellipse([dx-2, dy-2, dx+2, dy+2], fill=(70, 70, 75))

    # Add frame
    builder.add_frame(frame)

# Save the GIF
output_path = '/Users/han/dev/git_repos/dotfiles/claude/skills/skills_vs_mcps.gif'
info = builder.save(output_path, num_colors=128)
print(f"\nGIF saved to: {output_path}")
