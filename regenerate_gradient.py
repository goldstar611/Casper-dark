#!/usr/bin/env python3
"""
Generate publication-cover.jpg gradient from scratch
Creates a gradient from dark blue to dark grey
"""

from PIL import Image
import numpy as np

def regenerate_gradient(width=5000, height=3500):
    """
    Generate a gradient image from dark blue to dark grey
    
    Args:
        width: Image width in pixels (default 5000)
        height: Image height in pixels (default 3500)
    """
    # Define target colors
    dark_blue = np.array([35, 50, 110], dtype=np.float32)
    dark_grey = np.array([70, 70, 70], dtype=np.float32)
    
    # Create image array
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Generate diagonal gradient from top-left to bottom-right
    for y in range(height):
        for x in range(width):
            # Calculate blend factor (0 at top-left, 1 at bottom-right)
            # Normalize x and y to 0-1 range
            norm_x = x / (width - 1)
            norm_y = y / (height - 1)
            
            # Use average of x and y for diagonal blend
            blend = (norm_x + norm_y) / 2
            
            # Interpolate between dark blue and dark grey
            color = dark_blue * (1 - blend) + dark_grey * blend
            
            # Apply color to pixel
            img[y, x, :] = color.astype(np.uint8)
    
    # Save the image
    img_pil = Image.fromarray(img)
    img_pil.save('publication-cover.jpg', 'JPEG', quality=95)
    print("✓ Gradient image generated successfully!")
    print(f"✓ Dimensions: {width}x{height}")
    print("✓ Gradient: Top-Left (Dark Blue) → Bottom-Right (Dark Grey)")
    
    # Verify the colors
    new_array = np.array(Image.open('publication-cover.jpg'))
    print(f"\nGenerated colors:")
    print(f"  Top-left (dark blue):      {new_array[0, 0]}")
    print(f"  Center:                    {new_array[height//2, width//2]}")
    print(f"  Bottom-right (dark grey):  {new_array[-1, -1]}")

if __name__ == '__main__':
    regenerate_gradient()
