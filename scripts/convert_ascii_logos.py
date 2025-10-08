#!/usr/bin/env python3
"""Convert ASCII art logos to PNG images."""

from PIL import Image, ImageDraw, ImageFont
import os

# Logo designs
logos = {
    'shield_logo': """    ╔═══════════════════════╗
    ║      **[MISSION]**     ║
    ║    🛡️ 🔒 ⚪           ║
    ║   🔵⚪🔵🔵⚪🔵        ║
    ║  🔵  VOLLEYBALL  🔵   ║
    ║   🔵  AS SHIELD  🔵    ║
    ║    🔵🔵⚪🔵🔵⚪       ║
    ║       🏐🛡️            ║
    ║   **[IMPASSIBLES]**    ║
    ╚═══════════════════════╝""",

    'honey_badger_logo': """    ┌─────────────────────────┐
    │    😎 HONEY BADGER      │
    │      /           \      │
    │     /   M I 🏐   \     │
    │    |   JERSEY    |     │
    │     \           /      │
    │      \_________/       │
    │    LASER NET BEHIND    │
    │  MISSION IMPASSIBLES   │
    └─────────────────────────┘""",

    'vertical_logo': """    ┌─────────────────────────┐
    │                         │
    │     M I S S I O N       │
    │                         │
    │    IMPASSIBLES          │
    │     I         I 🏐     │
    │     I  VOLLEY  I       │
    │     I   BALL   I       │
    │     I         I        │
    │                         │
    └─────────────────────────┘""",

    'spike_logo': """    ┌─────────────────────────┐
    │                         │
    │      🏐  SPIKE!         │
    │        \                │
    │    🚫  \                │
    │  BLOCKER  \             │
    │   (JUMPING) \           │
    │      |       \          │
    │======NET=======---------│
    │   MISSION IMPASSIBLES   │
    └─────────────────────────┘"""
}

def create_ascii_image(text, output_path, bg_color='white', text_color='black'):
    """Create an image from ASCII art text."""

    # Use a monospace font for proper alignment
    try:
        # Try to use a system monospace font
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 16)
    except:
        # Fallback to default font
        font = ImageFont.load_default()

    # Calculate image size based on text
    lines = text.split('\n')
    max_width = max(len(line) for line in lines)

    # Create image with padding
    char_width = 10  # approximate width per character
    char_height = 20  # approximate height per line

    img_width = max_width * char_width + 40
    img_height = len(lines) * char_height + 40

    # Create image
    image = Image.new('RGB', (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(image)

    # Draw text
    y_position = 20
    for line in lines:
        draw.text((20, y_position), line, fill=text_color, font=font)
        y_position += char_height

    # Save image
    image.save(output_path)
    print(f"Created: {output_path}")

# Create output directory
output_dir = '/mnt/github/workspace-hub/hobbies/sports/volleyball/mission_impassibles/logo'
os.makedirs(output_dir, exist_ok=True)

# Generate images
for name, ascii_art in logos.items():
    output_path = os.path.join(output_dir, f'{name}.png')
    create_ascii_image(ascii_art, output_path)

print("\nAll logos converted successfully!")
