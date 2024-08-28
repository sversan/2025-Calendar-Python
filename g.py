import calendar
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# List of months
months = list(calendar.month_name)[1:]

# Load the mountain image
image_path = '22.jpg'  # Replace with the path to your JPEG image
img = mpimg.imread(image_path)

# Creating a single page with all months of 2025
plt.figure(figsize=(12, 14))
plt.suptitle("2025 CALENDAR - SEE YOU AT WORK", fontsize=24,color='green', weight='bold')

for month in range(1, 13):
    # Create a calendar for the month
    cal_str = calendar.month(2025, month)
    
    # Add each month's calendar to a subplot
    ax = plt.subplot(4, 3, month)
    plt.axis('off')
    plt.text(0.5, 0.7, cal_str, fontsize=10, ha='center', va='center', family='monospace')
   # plt.title(f"{months[month-1]}", fontsize=10, weight='bold')
    
    # Place the image below the calendar
    plt.imshow(img, aspect='auto', extent=[0.2, 0.8, 0, 0.5], zorder=-1)
    
# Adjust layout and show the plot
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
