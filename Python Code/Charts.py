import matplotlib.pyplot as plt
import numpy as np
import cv2
from io import BytesIO

# Categories and module data
difficulty_levels = ['Easy', 'Moderate', 'Hard']
preprocessing = [98.222, 98.963, 99.210]
classification = [96.420, 96.272, 96.593]
diff_classification = [82.000, 10.000, 24.000]
total_accuracy = [88.353, 52.637, 59.915]

# Bar positions
x = np.arange(len(difficulty_levels))
width = 0.2

# Create plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(x - 1.5*width, preprocessing, width, label='Image Pre-Processing')
ax.bar(x - 0.5*width, classification, width, label='Classification')
ax.bar(x + 0.5*width, diff_classification, width, label='Difficulty Classification')
ax.bar(x + 1.5*width, total_accuracy, width, label='Total Accuracy')

# Annotate
for i, accs in enumerate([preprocessing, classification, diff_classification, total_accuracy]):
    for j, val in enumerate(accs):
        ax.text(x[j] + (i - 1.5)*width, val + 1.5, f'{val:.1f}%', ha='center', fontsize=8)

# Formatting
ax.set_ylabel('Accuracy (%)')
ax.set_title('Module-wise Accuracy by Difficulty Level')
ax.set_xticks(x)
ax.set_xticklabels(difficulty_levels)
ax.set_ylim(0, 110)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Convert to OpenCV-compatible image
buf = BytesIO()
plt.savefig(buf, format='png')
plt.close(fig)
buf.seek(0)
img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
img = cv2.imdecode(img_arr, 1)

# Show plot using OpenCV
cv2.imshow('Project Module Accuracies', img)
cv2.waitKey(0)
cv2.destroyAllWindows()