import gmplot


def make_heat_map():
    APIKey_Addr = "keys/APIkey_DO_NOT_UPLOAD.txt"
    f = open(APIKey_Addr)
    apikey = f.read()
    f.close()
    print("API Key retrived as: " + apikey)

    gmap = gmplot.GoogleMapPlotter(40.818613232611334, -96.70261993245407, 17, apikey=apikey, map_type='hybrid')

    locations = {
        "UNL_Library": [40.81796773733276, -96.70261456803614],
        "UNL_Cornhusking_Tournament": [40.819076036680364, -96.70392348602881],
        "UNL_Memorial_Stadium": [40.82071221961654, -96.7056209734881],
        "UNL_Selleck_Quadrangle": [40.81906394481086, -96.69955090265869],
        "UNL_College_Of_Business": [40.820513231658445, -96.70050040464281],
        "UNL_Mueller_Tower": [40.82014163349815, -96.7025553177005],
        "UNL_Wood_Arts_Building": [40.8178418369227, -96.7050182258001],
        "UNL_Brace_Labratory": [40.81816255609379, -96.70649880517263]
    }

    heat_coords = [
        [40.81966654539061, -96.7055723448054],
        [40.821589448280555, -96.70567676817872],
        [40.818713592137485, -96.70219034951317],
        [40.819817152860274, -96.70189667599169],
        [40.81882854723606, -96.6993650077029],
        [40.82245180644226, -96.6966335293955],
        [40.81681287924564, -96.70576545076612],
        [40.81770028102595, -96.70587740505067],
        [40.81761379044568, -96.70443665609423],
        [40.8189170882565, -96.70663874544658],
        [40.819686235605076, -96.70362498854449],
        [40.818401941914466, -96.6997746822165],
        [40.81950550782203, -96.69933923527084],
        [40.81752827254301, -96.70497979224564],
        [40.81673889469543, -96.70501017227666],
        [40.81795744488268, -96.70566840604192],
        [40.82047877644389, -96.70591144620509],
        [40.819735415112255, -96.70507093233323],
        [40.81879279031017, -96.70470637209962],
        [40.82407284935278, -96.70085823622053],
        [40.82503072502059, -96.69972404882715],
        [40.81760668955854, -96.70042495123292]
    ]

    coord_list = []
    weights = []
    for key in locations:
        coord_list.append(locations[key])
        # print(key)
        if key == 'UNL_Cornhusking_Tournament':
            html_info = '<img src="map_info_html_files/UNL_Cornhusking_Tournament/UNL_Cornhusking_Tournament.png" alt="Cornhusking event info" width="500" height="300">'
        else:
            info_string = "<iframe src='./map_info_html_files/{file}/{file}.html' style='border:none;height:450px;width:408px;'></iframe>"
            html_info = info_string.format(file=key)
        # print(html_info)
        gmap.marker(locations[key][0], locations[key][1], color='white', info_window=html_info)
        weights.append(4)

    #  height='500' width='408'
    # html_info = "<iframe src='./map_info_html_files/Memorial_Stadium.html' style='border:none;height:450px;width:408px;'></iframe>"
    # gmap.marker(locations["UNL_Memorial_Stadium"][0], locations["UNL_Memorial_Stadium"][1], color='red', info_window=html_info)

    # print(coord_list)
    for coord in heat_coords:
        coord_list.append(coord)
    coords_list_weights = [2]* len(heat_coords)
    # print(len(heat_coords))
    # print(coords_list_weights)
    for weight in coords_list_weights:
        weights.append(weight)
    # print(weights)
    # print(len(weights))
    attractions = zip(*coord_list)

    # attractions = zip(*[
    #     (37.769901, -122.498331),
    #     (37.768645, -122.475328),
    #     (37.771478, -122.468677),
    #     (37.769867, -122.466102),
    #     (37.767187, -122.467496),
    #     (37.770104, -122.470436)
    # ])

    gmap.heatmap(
        *attractions,
        radius=60,
        weights=weights,
        max_intensity=2,
        gradient=[(0, 0, 255, 0), (0, 255, 0, 0.9), (255, 0, 0, 1)]
    )

    gmap.draw('generated_files/map_secret.html')