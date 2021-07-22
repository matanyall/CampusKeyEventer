import gmplot

APIKey_Addr = "APIkey_DO_NOT_UPLOAD.txt"
f = open(APIKey_Addr)
apikey = f.read()
f.close()
print("API Key retrived as: " + apikey)

gmap = gmplot.GoogleMapPlotter(40.818613232611334, -96.70261993245407, 17, apikey=apikey)

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

coord_list = []

for key in locations:
    coord_list.append(locations[key])
    gmap.marker(locations[key][0], locations[key][1], color='red', info_window=key)

# print(coord_list)


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
    radius=40,
    weights=[5, 1, 1, 1, 3, 1, 1, 5],
    gradient=[(0, 0, 255, 0), (0, 255, 0, 0.9), (255, 0, 0, 1)]
)

gmap.draw('map.html')