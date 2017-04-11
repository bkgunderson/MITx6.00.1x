import csv

# open csv files
songFile = open('songs.csv', "rb")
liturgicalFile = open('liturgical.csv', "rb")

if songFile and liturgicalFile:
    song_reader = csv.reader(songFile)
    liturgical_reader = csv.reader(liturgicalFile)

    song_row = 0
    header_dict = {}
    song_dict = {}
    song_name = 0
    for row in song_reader:
        if song_row == 0:
            header = row
            cell_num = 0
            for cell in header:
                header_dict[cell] = cell_num
                if cell == 'name':
                    song_name = cell_num
                cell_num += 1
        elif len(row) > 1:
            song_id = row[header_dict['id']]
            if row[header_dict['name']]:
                song_dict[song_id] = row
        song_row += 1

    lit_row = 0
    header_dict = {}
    lit_dict = {}
    lit_name = 0
    for row in liturgical_reader:
        if lit_row == 0:
            header = row
            cell_num = 0
            for cell in header:
                header_dict[cell] = cell_num
                if cell == 'name':
                    lit_name = cell_num
                cell_num += 1
        elif len(row) > 1:
            lit_id = row[header_dict['id']]
            if row[header_dict['name']]:
                lit_dict[lit_id] = row
        lit_row += 1

    # Print the name of the each liturgical tag.
    # Find which songs have this liturgical tag and print them underneath the tag.
    for item in lit_dict:
        print lit_dict[item][lit_name]
        for song in song_dict:
            if song_dict[song][7]:
                ids = song_dict[song][7]
                ids = ids.split(',')
                for lit_tag in ids:
                    if lit_tag == item:
                        print "- %s" % song_dict[song][song_name]

    songFile.close()
    liturgicalFile.close()
