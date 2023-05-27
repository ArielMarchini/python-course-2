def parse_ranges(ranges_string):
    range_segments = ranges_string.split(',')
    first_generator = (segment.split('-') for segment in range_segments)
    second_generator = (num for start, stop in first_generator for num in range(int(start), int(stop) + 1))
    return second_generator
