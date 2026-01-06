# Adding YouTube Videos to Presentations

This guide explains how to add YouTube videos to your MFM presentations.

## Step 1: Upload Your Video to YouTube

1. Go to [YouTube Studio](https://studio.youtube.com/)
2. Click "Create" → "Upload videos"
3. Upload your MP4 file
4. Set the video visibility:
   - **Public**: Anyone can find and watch
   - **Unlisted**: Only people with the link can watch (recommended for educational content)
   - **Private**: Only you and people you invite can watch
5. Once uploaded, get the video ID from the URL:
   - Example URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   - Video ID: `dQw4w9WgXcQ`

## Step 2: Add Video to Your Presentation Card

To add a video to any presentation, edit `index.html` and modify the card:

### Example - Card WITHOUT Video (Before):
```html
<div class="card">
  <h2>Short Interval Pregnancy - Patient Counseling</h2>
  <p>Patient education on short interpregnancy intervals...</p>
  <div>
    <span class="tag">Interpregnancy Interval</span>
    <span class="tag">Family Planning</span>
    <span class="tag">Patient Education</span>
  </div>
  <a href="decks/short-interval-pregnancy/short-interval.html" class="btn">View Presentation</a>
</div>
```

### Example - Card WITH Video (After):
```html
<div class="card has-video">
  <h2>Short Interval Pregnancy - Patient Counseling</h2>
  <p>Patient education on short interpregnancy intervals...</p>
  <div>
    <span class="video-badge">Video Available</span>
    <span class="tag">Interpregnancy Interval</span>
    <span class="tag">Family Planning</span>
    <span class="tag">Patient Education</span>
  </div>
  <div class="button-group">
    <a href="decks/short-interval-pregnancy/short-interval.html" class="btn">View Presentation</a>
    <a href="https://www.youtube.com/watch?v=YOUR_VIDEO_ID" target="_blank" class="btn btn-video">Watch Video</a>
  </div>
</div>
```

## Key Changes to Make:

1. **Add `has-video` class to the card**:
   ```html
   <div class="card has-video">
   ```

2. **Add video badge** (place it before the tags):
   ```html
   <span class="video-badge">Video Available</span>
   ```

3. **Wrap buttons in `button-group` div**:
   ```html
   <div class="button-group">
     <a href="..." class="btn">View Presentation</a>
     <a href="https://www.youtube.com/watch?v=YOUR_VIDEO_ID" target="_blank" class="btn btn-video">Watch Video</a>
   </div>
   ```

4. **Replace `YOUR_VIDEO_ID`** with your actual YouTube video ID

## Visual Indicators

When you add a video:
- Card will have a **red glow border** on hover
- **🎥 Video Available** badge appears before tags
- **🎥 Watch Video** button appears in red next to the presentation button

## Alternative: Embed Video in Presentation Page

You can also embed the YouTube video directly in your presentation HTML files:

```html
<div style="max-width: 800px; margin: 40px auto;">
  <h3>Watch the Video</h3>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
    <iframe 
      style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
      src="https://www.youtube.com/embed/YOUR_VIDEO_ID" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
    </iframe>
  </div>
</div>
```

## Quick Reference

- **YouTube Upload**: https://studio.youtube.com/
- **Video ID Location**: URL after `watch?v=`
- **Card Class**: Add `has-video`
- **Badge**: `<span class="video-badge">Video Available</span>`
- **Button**: `<a href="https://www.youtube.com/watch?v=ID" target="_blank" class="btn btn-video">Watch Video</a>`

## Need Help?

If you need assistance adding videos to specific presentations, just let me know which presentations you want to add videos to, and I can update them for you!
