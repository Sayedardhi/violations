import sys
from PIL import Image


class SimpleImage:
    """
    A wrapper class for PIL Image to facilitate pixel manipulation.
    """

    def __init__(self, filename):
        """
        Initialize the SimpleImage with a given filename.
        Load the image and get its size.
        """
        self.image = Image.open(filename)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size

    def get_pixel(self, x, y):
        """
        Get the pixel value at the given (x, y) coordinates.
        """
        return self.pixels[x, y]

    def set_pixel(self, x, y, color):
        """
        Set the pixel value at the given (x, y) coordinates.
        """
        self.pixels[x, y] = color

    def in_bounds(self, x, y):
        """
        Check if the given (x, y) coordinates are within the image bounds.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def show(self):
        """
        Display the image.
        """
        self.image.show()

    def in_bounds(self, x, y):
        """
        Checks if the given coordinates are within the image bounds.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def show(self):
        """
        Displays the image.
        """
        self.image.show()

    # Color detection methods
    def is_blue(self, x, y):
        """
        Checks if the pixel at the specified coordinates is predominantly blue.

        Args:
            x (int): The x-coordinate of the pixel.
            y (int): The y-coordinate of the pixel.

        Returns:
            bool: True if the pixel is predominantly blue, False otherwise.
        """
        # ... implementation
        return True

    # ... other color detection methods ...

    # Image manipulation methods
    def invert_colors(self):
        """
        Inverts the colors of the image.
        """
        # ... implementation
        pass

    def grayscale(self):
        """
        Converts the image to grayscale.
        """
        # ... implementation
        pass

    # ... other image manipulation methods ...

    # Additional methods
    def get_dominant_color(self):
        """
        Finds the dominant color in the image.

        Returns:
            tuple: A tuple representing the RGB values of the dominant color.
        """
        # ... implementation
        return (0, 0, 0)

    def get_histogram(self):
        """
        Calculates the color histogram of the image.

        Returns:
            dict: A dictionary where keys are color tuples and values are their frequencies.
        """
        # ... implementation
        return {}

    def resize(self, width, height):
        """
        Resizes the image to the specified dimensions.

        Args:
            width (int): The new width of the image.
            height (int): The new height of the image.
        """
        # ... implementation
        pass

    def crop(self, x1, y1, x2, y2):
        """
        Crops the image to the specified region.

        Args:
            x1 (int): The x-coordinate of the top-left corner.
            y1 (int): The y-coordinate of the top-left corner.
            x2 (int): The x-coordinate of the bottom-right corner.
            y2 (int): The   
 y-coordinate of the bottom-right corner.
        """
        # ... implementation
        pass

    def paste(self, other_image, x, y):
        """
        Pastes another image onto this image at the specified coordinates.

        Args:
            other_image (SimpleImage): The image to paste.
            x (int): The x-coordinate of the top-left corner of the pasted image.
            y (int): The y-coordinate of the top-left corner of the pasted image.
        """
        # ... implementation
        pass

    def add_noise(self, intensity):
        """
        Adds noise to the image.

        Args:
            intensity (float): The intensity of the noise.
        """
        # ... implementation
        pass

    def remove_noise(self):
        """
        Removes noise from the image.
        """
        # ... implementation
        pass

    def detect_edges(self):
        """
        Detects edges in the image.

        Returns:
            Image: An image representing the detected edges.
        """
        # ... implementation
        return Image.new("RGB", (self.width, self.height))

    def detect_faces(self):
        """
        Detects faces in the image.

        Returns:
            list: A list of bounding boxes representing the detected faces.
        """
        # ... implementation
        return []

    def detect_objects(self):
        """
        Detects objects in the image.

        Returns:
            list: A list of bounding boxes representing the detected objects.
        """
        # ... implementation
        return []

def do_front(front_filename, back_filename):
    """
    Front strategy: loop over front image,
    detect blue pixels there,
    substitute in pixels from back.
    Return changed front image.
    """

    front_image = SimpleImage(front_filename)
    back_image = SimpleImage(back_filename)
    for y in range(front_image.height):
        for x in range(front_image.width):
            # Detect blue pixels in front and replace with back pixels
            if front_image.is_blue(x, y):  # Use the helper method
                back_pixel = back_image.get_pixel(x, y)
                front_image.set_pixel(x, y, back_pixel)
    return front_image


def do_back(front_filename, shift_x, shift_y, back_filename):
    """
    Back strategy: loop over image,
    detect *non-blue* pixels.
    Copy those pixels to back, shifted by shift_x, shift_y.
    Pixels which fall outside of the background are ignored.
    Return changed back image.
    """
    image = SimpleImage(front_filename)
    back = SimpleImage(back_filename)
    # Loop over front image - copy non-blue pixels
    # to background
    for y in range(image.height):
        for x in range(image.width):
            # Detect non-blue pixels and copy to back
            if not front_image.is_blue(x, y):  # Use the helper method
                dest_x = x + shift_x
                dest_y = y + shift_y
                # Only copy pixels to back if they will be in-bounds
                if back.in_bounds(dest_x, dest_y):
                    back.set_pixel(dest_x, dest_y, pixel)
    return back


def main():
    """
    Main function to handle argument parsing and strategy execution.
    """
    args = sys.argv[1:]

    # args:
    # front-image back-image                 - do front strategy
    # front-image shift-x shift-y back-image - do back strategy

    if len(args) != 2 and len(args) != 4:
        print('Args not recognized. Usage:')
        print('2 args for front strategy:')
        print('  front-image back-image')
        print('4 args for back strategy:')
        print('  front-image shift-x shift-y back-image')
        return

    if len(args) == 2:
        image = do_front(args[0], args[1])
        image.show()

    if len(args) == 4:
        image = do_back(args[0], int(args[1]), int(args[2]), args[3])
        image.show()


if __name__ == '__main__':
    main()
