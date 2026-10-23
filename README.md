# Math Painting

An object-oriented Python application that lets users create customized image canvases and draw geometric shapes (rectangles and squares) with custom RGB colors interactively via the command line.

---

## Features

- **Custom Canvas**: Configure custom canvas width, height, and background color (`black` or `white`).
- **Interactive Shape Drawing**:
  - **Rectangle**: Specify start coordinates (`x`, `y`), width, height, and RGB color.
  - **Square**: Specify start coordinates (`x`, `y`), side length, and RGB color.
- **Image Generation**: Generates and saves the final composite image as `canvas.png` using NumPy and Pillow (PIL).
- **OOP Architecture**: Modular class-based design separating canvas rendering and shape logic.

---

## Project Structure

```text
├── canvas.py          # Canvas class for grid representation & image export
├── shapes.py          # Shape base class and Rectangle / Square implementations
├── main.py            # CLI entry point handling user interaction and canvas rendering
├── design.txt         # Initial requirements and object design specifications
├── requirements.txt   # Python package dependencies
└── README.md          # Project documentation
```

---

## Requirements

- Python 3.9+
- NumPy
- Pillow (PIL)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd math-painting
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the main application script:

```bash
python main.py
```

### Example Walkthrough

```text
Enter canvas width: 1000
Enter canvas height: 1000
Enter canvas color (white or black): white
What do you like to draw? Enter quit to quit: rectangle
Enter x of the Rectangle: 100
Enter y of the Rectangle: 200
How much red should the Rectangle have? 255
How much green should the Rectangle have? 0
How much blue should the Rectangle have? 0
Enter the width of the Rectangle: 300
Enter the height of the Rectangle: 150
What do you like to draw? Enter quit to quit: square
Enter x of the Square: 500
Enter y of the Square: 500
How much red should the Square have? 0
How much green should the Square have? 200
How much blue should the Square have? 50
Enter the side length of the Square: 200
What do you like to draw? Enter quit to quit: quit
```

After typing `quit`, the output image is saved as `canvas.png` in the project root.
