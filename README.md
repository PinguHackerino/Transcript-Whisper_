# 🎤 Simple Whisper Transcription Tool

A beginner-friendly tool to transcribe audio files using OpenAI Whisper.

## 📋 About This Project

This project is **currently in development** and was created by someone who's just starting to learn serious programming. The goal is simple: make Whisper transcription easy for everyone to use, even if you're not tech-savvy.

I'm learning as I go, so the code might not be perfect, but it works! The idea is to create something that anyone can download and use without complicated setup.

I’m also learning English, so if you notice some strange phrasing, that’s normal.

## ✨ What It Does Right Now

- 🖱️ **Easy file selection**: Just click to pick your audio file
- 🇮🇹 **Italian transcription**: Set up for Italian language (easy to change)
- ⚡ **Uses your GPU**: Automatically uses your graphics card if you have one
- 💾 **Saves your text**: Saves the transcription as a .txt file
- ⏱️ **Shows timing**: Tells you how long it took
- 🚨 **Error logging**: Saves error details to help fix problems

## 🔧 What You Need

### Software:
- Python 3.7 or newer (i would recommed Py 3.10.9)
- That's basically it! The script will tell you what else to install.

### To install the required stuff:
```
pip install torch
pip install openai-whisper
```

### Your computer should have:
- **Graphics card**: NVIDIA GPU is great but not required
- **RAM**: At least 4GB free
- **Internet**: To download the AI model (first time only)


## 🚀 How to Use It

1. **First time? Check your setup**:
   ```
   python check_cuda.py
   ```
   This helps you understand if everything is working and whether you can use GPU or CPU processing.

2. **Run the transcription tool**:
   ```
   python transcribe.py
   ```

3. **Pick your audio file** when the window opens

4. **Wait** while it transcribes (first time takes longer, and it depends which model you are using)

5. **Save your transcription** where you want it

## 📽️ Audio Files That Work

- MP3 files
- WAV files  
- M4A files
- MP4 files (audio part)

## 🔄 Development Status

### ✅ Working Right Now:
- [x] Basic file picker
- [x] Audio transcription
- [x] GPU support (if available)
- [x] Saves transcription to file
- [x] Error handling

### WIP:
- [ ] Automatic FFmpeg check/install
- [ ] Choose different AI models (small, medium, large)
- [ ] Better interface
- [ ] Process multiple files at once
- [ ] Different languages

### Maybe for the future:
- [ ] Video files
- [ ] Subtitle files
- [ ] Better text formatting
- [ ] Better error handling

## ⚠️ Things to Know

- **First time**: Downloads AI model (takes a while, be patient!)
- **GPU helps**: Much faster with a good graphics card
- **File size**: Really long audio files need more RAM
- **Audio quality**: Clear audio = better transcription

## 🐛 If Something Goes Wrong

### Common issues:
- **No GPU**: That's fine, it'll use your regular processor
- **File not found**: Make sure you picked a real file
- **Out of memory**: Try a shorter audio file

### Error logs:
When something breaks, check the `error_log.txt` file that gets created.

## 🤝 Help and Contributions

Since I'm still learning, any help is welcome! If you know how to code and see something that could be better, please let me know.

If you find bugs or have ideas, I'd love to hear them.

## 📝 Learning Notes

This is my first "real" programming project, so:
- The code might not be the most elegant
- I'm learning best practices as I go
- Comments in the code are sometimes in Italian (sorry!)
- I'm trying to make it work first, then make it pretty

---

*Made by someone learning to code, trying to make AI transcription simple for everyone.*
