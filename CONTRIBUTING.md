# Contributing to The Council of Chalcedon - Visual Novel

First off, **thank you** for considering contributing! I truly believe in open source and the power of community collaboration. Unlike many repositories, I actively welcome contributions of all kinds - from bug fixes to new features to historical research.

## My Promise to Contributors

- **I will respond to every PR and issue** - I guarantee feedback on all contributions
- **Bug fixes are obvious accepts** - If it fixes a bug, it's getting merged
- **New features are welcome** - I'm genuinely open to new ideas and enhancements
- **Historical corrections doubly welcome** - If you spot an inaccuracy in the dialogue or context, please let me know
- **Direct line of communication** - If I'm not responding to a PR or issue, email me directly at johnvondrashek@gmail.com

## How to Contribute

### Reporting Bugs

1. **Check existing issues** to avoid duplicates
2. **Open a new issue** with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Ren'Py version, etc.)

### Historical Corrections

The dialogue is based on the [Council of Chalcedon records](https://www.newadvent.org/fathers/3811.htm). If you notice:
- Misattributed quotes
- Historical inaccuracies
- Theological misrepresentations
- Missing context that would enhance understanding

Please open an issue or PR! Accuracy matters for an educational project like this.

### Suggesting Features

I'm open to new features! When suggesting:
1. Explain the problem you're trying to solve
2. Describe your proposed solution
3. Consider if it fits the project's educational mission

Ideas that might be especially welcome:
- Additional glossary entries for theological terms
- Improved session summaries
- Accessibility enhancements
- Localization/translation support

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test in Ren'Py Launcher
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

That's it! I'll review it and provide feedback.

## Development Setup

### Prerequisites

- [Ren'Py](https://www.renpy.org/latest.html) (8.0 or later)

### Running from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/JohnVonDrashek/council-of-chalcedon-vn.git
   ```
2. Open Ren'Py Launcher
3. Click "preferences" and add the cloned directory to your projects
4. Select "The Council of Chalcedon" from the project list
5. Click "Launch Project"

### Project Structure

```
game/
├── scripts/
│   ├── prologue/           # Historical context (428-451 AD)
│   ├── act1_procedural/    # Sessions I-III
│   ├── act2_doctrinal/     # Sessions IV-V
│   └── act3_institutional/ # Sessions VI-XV + Canons
├── images/                 # Character sprites and backgrounds
├── audio/                  # Music and sound effects
└── gui/                    # UI elements
```

### Your First Contribution

Never contributed to open source before? No problem! Look for issues labeled `good first issue` or `help wanted`. Resources:
- [How to Make a Pull Request](http://makeapullrequest.com/)
- [First Timers Only](https://www.firsttimersonly.com/)

Some beginner-friendly contributions:
- Fixing typos in dialogue
- Adding glossary definitions
- Improving documentation
- Testing on different platforms

## Code Style

### Ren'Py Scripts

- Use 4 spaces for indentation
- Keep dialogue lines readable (break long speeches across multiple lines)
- Comment complex logic or historical context
- Use descriptive label names (e.g., `session_03_verdict` not `s3v`)

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Reference issue numbers when applicable (`Fix #123`)

## Code of Conduct

This project follows the [Rule of St. Benedict](CODE_OF_CONDUCT.md) as its code of conduct. Please read it - it's been guiding communities for over 1,500 years. The key points:
- Love your neighbor as yourself
- Do not return evil for evil
- Bear patiently wrongs done to yourself
- Never despair of God's mercy

## Questions?

- Open an issue
- Email me: johnvondrashek@gmail.com

I appreciate every contribution, big or small. Thank you for helping bring church history to life!

---

*"For where two or three gather in my name, there am I with them."* - Matthew 18:20
