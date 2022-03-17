def calculate_adjusted_length(exact_length, corner_cut, mid_foot_width):
    """
    2*mid_foot_width is subtracted from adjusted_length to
    account for the extra 1.5 inches on each end foot width.
    """
    if corner_cut == True:
        adjusted_length = exact_length - 4.5
    elif corner_cut == False:
        adjusted_length = exact_length

    adjusted_length = adjusted_length - (2 * mid_foot_width)

    return adjusted_length

def calculate_num_sections(adjusted_length):
    """
    Calculate the number of sections that need to be cut.
    """
    num_sections = round(adjusted_length / 36.0)

    return num_sections

def calculate_variable_cut_lengths(adjusted_length, num_sections):
    """
    Calculates the topshelf and crossbar lengths which vary for every wall.

    1/8 is removed between each section to account for the slight gap
    caused by installation.

    1/8 is also removed between each crossbar to allow easier installation.
    """
    adjusted_length = adjusted_length - num_sections * (1 / 8)

    topshelf_midpiece_length = adjusted_length / num_sections
    if num_sections > 1:
        topshelf_endpiece_length = topshelf_midpiece_length + 1.5
    else:
        topshelf_endpiece_length = topshelf_midpiece_length + 3

    topshelf_cornerpiece_length = topshelf_endpiece_length + 4.5

    crossbar_length = topshelf_midpiece_length - (3 + 1 / 8)

    return (
        topshelf_midpiece_length,
        topshelf_endpiece_length,
        topshelf_cornerpiece_length,
        crossbar_length,
    )

def calculate_number_of_each_cut(num_sections, corner_cut):
    """
    Calculates the number of fixed and variable cuts:

    Variable Cuts:
    Topshelf Midpiece
    Topshelf Endpiece
    Topshelf Cornerpiece
    Crossbar

    Fixed Cuts:
    End foot
    Mid foot
    """
    # fix me ------------------------------------------
    topshelf_midpiece_count = num_sections - 2
    if corner_cut == True:
        if num_sections > 1:
            topshelf_endpiece_count = 1
            topshelf_cornerpiece_count = 1
        else:
            topshelf_endpiece_count = 1
            topshelf_cornerpiece_count = 0
    elif corner_cut == False:
        if num_sections > 1:
            topshelf_endpiece_count = 2
            topshelf_cornerpiece_count = 0
        else:
            topshelf_endpiece_count = 1
            topshelf_cornerpiece_count = 0


    crossbar_count = num_sections

    end_foot_count = 2
    mid_foot_count = num_sections * 2 - 2
    return (
        topshelf_midpiece_count,
        topshelf_endpiece_count,
        topshelf_cornerpiece_count,
        crossbar_count,
        end_foot_count,
        mid_foot_count,
    )

    # fix me ------------------------------------------

def generate_cut_lengths(
    topshelf_midpiece_count,
    topshelf_endpiece_count,
    topshelf_cornerpiece_count,
    crossbar_count,
    end_foot_count,
    mid_foot_count,
    topshelf_midpiece_length,
    topshelf_endpiece_length,
    topshelf_cornerpiece_length,
    crossbar_length,
):
    """
    Generate counts and lengths for each of the cuts:
    Topshelf Midpiece
    Topshelf Endpiece
    Topshelf Cornerpiece
    Crossbar
    End foot
    Mid foot
    """
    output_list = [
        f'{topshelf_endpiece_count} - 1x5 @ {round(topshelf_endpiece_length, 3)}" - topshelf endpiece',
        f'{crossbar_count} - 1x6 @ {round(crossbar_length, 3)}" - crossbar',
        "",
        f'{mid_foot_count} - 1x2 @ 7.5" - topshelf mid foot',
        f'{end_foot_count} - 1x3 @ 7.5" - topshelf end foot',
    ]

    if topshelf_midpiece_count > 0:
        output_list.insert(
            0,
            f'{topshelf_midpiece_count} - 1x5 @ {round(topshelf_midpiece_length, 3)}" - topshelf midpiece',
        )
    else:
        pass

    if topshelf_cornerpiece_count > 0:
        output_list.insert(
            2,
            f'{topshelf_cornerpiece_count} - 1x5 @ {round(topshelf_cornerpiece_length, 3)}" - topshelf cornerpiece',
        )

    for i in output_list:
        print(i)
    print("\nnote - only accurate for lengths >= 62")
    print(
        "this is the inflection point for when topshelf midpiece goes from negative to 0"
    )
    print(
        "Is the reason for the error that the negative length is added to the total length?"
    )
