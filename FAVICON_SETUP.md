# Favicon Setup Instructions

## Recommended Image
Use **the first image** (fetus with heart icon) - it's more recognizable at small sizes and has better symbolism for MFM.

## Files You Need to Create

From your source image, you need to generate the following files:

### Required Files:
1. `favicon.ico` - 16x16 and 32x32 (multi-size .ico file)
2. `favicon-16x16.png` - 16x16 pixels
3. `favicon-32x32.png` - 32x32 pixels
4. `apple-touch-icon.png` - 180x180 pixels (for iOS)
5. `android-chrome-192x192.png` - 192x192 pixels
6. `android-chrome-512x512.png` - 512x512 pixels

## How to Generate These Files

### Option 1: Online Tool (Easiest)
1. Go to https://realfavicongenerator.net/
2. Upload your source image (the fetus with heart icon)
3. Customize if needed
4. Download the generated package
5. Extract all files to your project root directory

### Option 2: Using ImageMagick (Command Line)
If you have ImageMagick installed:

```bash
# Convert your source image to various sizes
magick convert source.png -resize 16x16 favicon-16x16.png
magick convert source.png -resize 32x32 favicon-32x32.png
magick convert source.png -resize 180x180 apple-touch-icon.png
magick convert source.png -resize 192x192 android-chrome-192x192.png
magick convert source.png -resize 512x512 android-chrome-512x512.png

# Create multi-size .ico file
magick convert source.png -resize 16x16 -resize 32x32 favicon.ico
```

### Option 3: Using Photoshop/GIMP
1. Open your source image
2. Resize and export each size individually
3. For .ico file, use a plugin or online converter

## Installation Steps

1. Generate all the favicon files using one of the methods above
2. Place all generated files in the root directory of your project
3. Copy the contents of `favicon-config.html` into the `<head>` section of your `index.html`
4. The `site.webmanifest` file is already created and configured

## What's Already Done

✅ `site.webmanifest` - Web app manifest for PWA support
✅ `favicon-config.html` - HTML code to add to your index.html

## What You Need to Do

1. Generate the image files (favicon.ico, PNGs)
2. Add the HTML from `favicon-config.html` to your `index.html` <head> section

## Testing

After installation, test your favicon on:
- Desktop browsers (Chrome, Firefox, Edge, Safari)
- iOS Safari (add to home screen)
- Android Chrome (add to home screen)

## Notes

- The fetus with heart icon is recommended because:
  - Clear symbolism for maternal-fetal medicine
  - Good contrast and visibility at small sizes
  - Distinctive shape that stands out in browser tabs
  - Heart element adds emotional connection
