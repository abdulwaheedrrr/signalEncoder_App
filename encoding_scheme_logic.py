import math

def _validate_binary_input(binary_input):
    """Internal helper to validate input for encoding functions."""
    if not isinstance(binary_input, str) or not all(bit in '01' for bit in binary_input):
        print("Error: Input must be a binary string containing only '0's and '1's.")
        return False
    return True

def nrz_l(binary_input):
   
    if not _validate_binary_input(binary_input):
        return []
    if not binary_input:
        return []

    signal_levels = []
    for bit in binary_input:
        if bit == '0':
            signal_levels.append(-1)  # Representing -V
        elif bit == '1':
            signal_levels.append(1)   # Representing +V
    return signal_levels

def nrz_i(binary_input, initial_level=1):
  
    if not _validate_binary_input(binary_input):
        return []
    if not binary_input:
        return []

    if initial_level not in [1, -1]:
        print(f"Warning: NRZ-I initial_level should be 1 or -1. Using default: 1")
        initial_level = 1

    signal_levels = []
    current_level = initial_level

    for bit in binary_input:
        if bit == '0':
            # No transition: level stays the same
            signal_levels.append(current_level)
        elif bit == '1':
            # Transition: invert the current level
            current_level *= -1 # Flip the level
            signal_levels.append(current_level)
    return signal_levels

def rz(binary_input):
 
    if not _validate_binary_input(binary_input):
        return []
    if not binary_input:
        return []

    signal_levels = []
    for bit in binary_input:
        if bit == '0':
            signal_levels.extend([-1, 0]) # -V for first half, 0 for second half
        elif bit == '1':
            signal_levels.extend([1, 0])  # +V for first half, 0 for second half
    return signal_levels

def manchester(binary_input):
   
    if not _validate_binary_input(binary_input):
        return []
    if not binary_input:
        return []

    signal_levels = []
    for bit in binary_input:
        if bit == '0':
            signal_levels.extend([1, -1]) # High then Low
        elif bit == '1':
            signal_levels.extend([-1, 1]) # Low then High
    return signal_levels

def differential_manchester(binary_input, initial_transition_is_lh=True):
   
    if not _validate_binary_input(binary_input):
        return []
    if not binary_input:
        return []

    signal_levels = []
   
    previous_transition_is_lh = initial_transition_is_lh

    for bit in binary_input:
        if bit == '0':
            if previous_transition_is_lh: # Previous ended High (+1)
                signal_levels.extend([-1, 1]) # Start Low, go High mid-bit
                previous_transition_is_lh = True # This bit was L-H
            else: # Previous ended Low (-1)
                signal_levels.extend([1, -1]) # Start High, go Low mid-bit
                previous_transition_is_lh = False # This bit was H-L
        elif bit == '1':
          
            if previous_transition_is_lh: # Previous ended High (+1)
                signal_levels.extend([1, -1]) # Start High, go Low mid-bit
                previous_transition_is_lh = False # This bit was H-L
            else: # Previous ended Low (-1)
                signal_levels.extend([-1, 1]) # Start Low, go High mid-bit
                previous_transition_is_lh = True # This bit was L-H
    return signal_levels

# --- Test Cases ---
if __name__ == "__main__":
    print("--- Testing All Encoding Schemes ---")
    print("Binary Input: 11001\n")

    test_input = "11001"

    # NRZ-L
    nrz_l_output = nrz_l(test_input)
    print(f"NRZ-L ('{test_input}'): {nrz_l_output}")

    # NRZ-I (with initial_level=1)
    nrz_i_output_pos_init = nrz_i(test_input, initial_level=1)
    print(f"NRZ-I ('{test_input}', init=+1): {nrz_i_output_pos_init}")

    # NRZ-I (with initial_level=-1)
    nrz_i_output_neg_init = nrz_i(test_input, initial_level=-1)
    print(f"NRZ-I ('{test_input}', init=-1): {nrz_i_output_neg_init}")
    # RZ
    rz_output = rz(test_input)
    print(f"RZ ('{test_input}'): {rz_output}")

    # Manchester
    manchester_output = manchester(test_input)
    print(f"Manchester ('{test_input}'): {manchester_output}")

    # Differential Manchester (with initial_transition_is_lh=True)
    dm_output_lh_init = differential_manchester(test_input, initial_transition_is_lh=True)
    print(f"Differential Manchester ('{test_input}', init_LH=True): {dm_output_lh_init}")

    # Differential Manchester (with initial_transition_is_lh=False)
    dm_output_hl_init = differential_manchester(test_input, initial_transition_is_lh=False)
    print(f"Differential Manchester ('{test_input}', init_LH=False): {dm_output_hl_init}")