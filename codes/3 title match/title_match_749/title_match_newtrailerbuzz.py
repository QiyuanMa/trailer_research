import json
import re
from title_match_749.datamanage_newtrailerbuzz import DataManager

db = DataManager()


def load_trailer():
    with open(r'C:\Users\student\Desktop\newtrailerbuzz_movie_trailer_merged_info.json', 'r', encoding='utf8') as trailer:
        trailer_data = json.load(trailer)
        return trailer_data


def load_movie():
    with open(r'C:\Users\student\Desktop\imdb_merged_trailerlist_info.json', 'r', encoding='utf8') as movie:
        movie_data = json.load(movie)
        return movie_data


if __name__ == "__main__":
    movie_data = load_movie()
    trailer_data = load_trailer()
    # print (movie_data)
    # movie info from imdb_2013trailerlist_info
    Title = []
    Title_link = []
    certificate = []
    lister_item_content = []
    ipl_rating_star_rating = []
    runtime = []
    lister_item_content1 = []
    genre = []
    inline_block = []
    Gross = []
    Headline = []
    Director = []
    Writers = []
    Stars = []
    Plot_Keywords = []
    Genres = []
    Parents_Guide = []
    Official_Sites = []
    Country = []
    Language = []
    Filming_Locations = []
    Gross_USA = []
    Cumulative_Worldwide_Gross = []
    Production_Co = []
    Sound_Mix = []
    Color = []
    Aspect_Ratio = []
    Description = []
    Trailer = []
    UK_Release_Time = []
    Budget = []
    US = []
    Writers_2 = []
    Stars_2 = []
    Stars_3 = []
    Storyline = []
    Plot_Keywords_2 = []
    Plot_Keywords_3 = []
    Plot_Keywords_4 = []
    Plot_Keywords_5 = []
    # trailer info from youtube_trailer_info_all
    title = []
    time = []
    channelId = []
    Trailer_series = []
    description = []
    categoryId = []
    duration = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    favoriteCount = []
    commentCount = []
    Stars = []
    Directors = []
    ReleaseTime = []
    Synopsis = []
    # transfer movie info into trailer info
    Movie_Title = []
    Movie_Title_link = []
    Movie_certificate = []
    Movie_lister_item_content = []
    Movie_ipl_rating_star_rating = []
    Movie_runtime = []
    Movie_lister_item_content1 = []
    Movie_genre = []
    Movie_inline_block = []
    Movie_Gross = []
    Movie_Headline = []
    Movie_Director = []
    Movie_Writers = []
    Movie_Stars = []
    Movie_Plot_Keywords = []
    Movie_Genres = []
    Movie_Parents_Guide = []
    Movie_Official_Sites = []
    Movie_Country = []
    Movie_Language = []
    Movie_Filming_Locations = []
    Movie_Gross_USA = []
    Movie_Cumulative_Worldwide_Gross = []
    Movie_Production_Co = []
    Movie_Sound_Mix = []
    Movie_Color = []
    Movie_Aspect_Ratio = []
    Movie_Description = []
    Movie_Trailer = []
    Movie_UK_Release_Time = []
    Movie_Budget = []
    Movie_US = []
    Movie_Writers_2 = []
    Movie_Stars_2 = []
    Movie_Stars_3 = []
    Movie_Storyline = []
    Movie_Plot_Keywords_2 = []
    Movie_Plot_Keywords_3 = []
    Movie_Plot_Keywords_4 = []
    Movie_Plot_Keywords_5 = []
    for i in range(749):
        # movie info from imdb_2013trailerlist_info
        Title.append(movie_data.get("RECORDS")[i].get("Title"))
        Title_link.append(movie_data.get("RECORDS")[i].get("Title_link"))
        certificate.append(movie_data.get("RECORDS")[i].get("certificate"))
        lister_item_content.append(movie_data.get("RECORDS")[i].get("lister-item-content"))
        ipl_rating_star_rating.append(movie_data.get("RECORDS")[i].get("ipl-rating-star__rating"))
        runtime.append(movie_data.get("RECORDS")[i].get("runtime"))
        lister_item_content1.append(movie_data.get("RECORDS")[i].get("lister-item-content1"))
        genre.append(movie_data.get("RECORDS")[i].get("genre"))
        inline_block.append(movie_data.get("RECORDS")[i].get("inline-block"))
        Gross.append(movie_data.get("RECORDS")[i].get("Gross"))
        Headline.append(movie_data.get("RECORDS")[i].get("Headline"))
        Director.append(movie_data.get("RECORDS")[i].get("Director"))
        Writers.append(movie_data.get("RECORDS")[i].get("Writers"))
        Stars.append(movie_data.get("RECORDS")[i].get("Stars"))
        Plot_Keywords.append(movie_data.get("RECORDS")[i].get("Plot Keywords"))
        Genres.append(movie_data.get("RECORDS")[i].get("Genres"))
        Parents_Guide.append(movie_data.get("RECORDS")[i].get("Parents Guide"))
        Official_Sites.append(movie_data.get("RECORDS")[i].get("Official Sites"))
        Country.append(movie_data.get("RECORDS")[i].get("Country"))
        Language.append(movie_data.get("RECORDS")[i].get("Language"))
        Filming_Locations.append(movie_data.get("RECORDS")[i].get("Filming Locations"))
        Gross_USA.append(movie_data.get("RECORDS")[i].get("Gross USA"))
        Cumulative_Worldwide_Gross.append(movie_data.get("RECORDS")[i].get("Cumulative Worldwide Gross"))
        Production_Co.append(movie_data.get("RECORDS")[i].get("Production Co"))
        Sound_Mix.append(movie_data.get("RECORDS")[i].get("Sound Mix"))
        Color.append(movie_data.get("RECORDS")[i].get("Color"))
        Aspect_Ratio.append(movie_data.get("RECORDS")[i].get("Aspect Ratio"))
        Description.append(movie_data.get("RECORDS")[i].get("Description"))
        Trailer.append(movie_data.get("RECORDS")[i].get("Trailer"))
        UK_Release_Time.append(movie_data.get("RECORDS")[i].get("UK Release Time"))
        Budget.append(movie_data.get("RECORDS")[i].get("Budget"))
        US.append(movie_data.get("RECORDS")[i].get("US"))
        Writers_2.append(movie_data.get("RECORDS")[i].get("Writers 2"))
        Stars_2.append(movie_data.get("RECORDS")[i].get("Stars 2"))
        Stars_3.append(movie_data.get("RECORDS")[i].get("Stars 3"))
        Storyline.append(movie_data.get("RECORDS")[i].get("Storyline"))
        Plot_Keywords_2.append(movie_data.get("RECORDS")[i].get("Plot Keywords 2"))
        Plot_Keywords_3.append(movie_data.get("RECORDS")[i].get("Plot Keywords 3"))
        Plot_Keywords_4.append(movie_data.get("RECORDS")[i].get("Plot Keywords 4"))
        Plot_Keywords_5.append(movie_data.get("RECORDS")[i].get("Plot Keywords 5"))

    for i in range(516):
        # trailer info from youtube_trailer_info_all
        title.append(trailer_data.get("RECORDS")[i].get("title"))
        time.append(trailer_data.get("RECORDS")[i].get("time"))
        channelId.append(trailer_data.get("RECORDS")[i].get("channelId"))
        Trailer_series.append(trailer_data.get("RECORDS")[i].get("Trailer_series"))
        description.append(trailer_data.get("RECORDS")[i].get("description"))
        categoryId.append(trailer_data.get("RECORDS")[i].get("categoryId"))
        duration.append(trailer_data.get("RECORDS")[i].get("duration"))
        viewCount.append(trailer_data.get("RECORDS")[i].get("viewCount"))
        likeCount.append(trailer_data.get("RECORDS")[i].get("likeCount"))
        dislikeCount.append(trailer_data.get("RECORDS")[i].get("dislikeCount"))
        favoriteCount.append(trailer_data.get("RECORDS")[i].get("favoriteCount"))
        commentCount.append(trailer_data.get("RECORDS")[i].get("commentCount"))
        Stars.append(trailer_data.get("RECORDS")[i].get("Stars"))
        Directors.append(trailer_data.get("RECORDS")[i].get("Directors"))
        ReleaseTime.append(trailer_data.get("RECORDS")[i].get("ReleaseTime"))
        Synopsis.append(trailer_data.get("RECORDS")[i].get("Synopsis"))
        Movie_Title.append(None)
        Movie_Title_link.append(None)
        Movie_certificate.append(None)
        Movie_lister_item_content.append(None)
        Movie_ipl_rating_star_rating.append(None)
        Movie_runtime.append(None)
        Movie_lister_item_content1.append(None)
        Movie_genre.append(None)
        Movie_inline_block.append(None)
        Movie_Gross.append(None)
        Movie_Headline.append(None)
        Movie_Director.append(None)
        Movie_Writers.append(None)
        Movie_Stars.append(None)
        Movie_Plot_Keywords.append(None)
        Movie_Genres.append(None)
        Movie_Parents_Guide.append(None)
        Movie_Official_Sites.append(None)
        Movie_Country.append(None)
        Movie_Language.append(None)
        Movie_Filming_Locations.append(None)
        Movie_Gross_USA.append(None)
        Movie_Cumulative_Worldwide_Gross.append(None)
        Movie_Production_Co.append(None)
        Movie_Sound_Mix.append(None)
        Movie_Color.append(None)
        Movie_Aspect_Ratio.append(None)
        Movie_Description.append(None)
        Movie_Trailer.append(None)
        Movie_UK_Release_Time.append(None)
        Movie_Budget.append(None)
        Movie_US.append(None)
        Movie_Writers_2.append(None)
        Movie_Stars_2.append(None)
        Movie_Stars_3.append(None)
        Movie_Storyline.append(None)
        Movie_Plot_Keywords_2.append(None)
        Movie_Plot_Keywords_3.append(None)
        Movie_Plot_Keywords_4.append(None)
        Movie_Plot_Keywords_5.append(None)
        # transfer movie info into trailer info
    # print(title)

    for i in range(len(title)):
        for j in range(1, len(Title)):
            if re.match(Title[j].upper(), title[i]) != None:
                # print(len(re.match(Title[j],title[i]).group()))
                if title[i][len(re.match(Title[j].upper(), title[i]).group())] != ':' and title[i][
                    len(re.match(Title[j].upper(), title[i]).group()) + 1] != 'I' and \
                        title[i][len(re.match(Title[j].upper(), title[i]).group()) + 1] != '2' and title[i][
                    len(re.match(Title[j].upper(), title[i]).group()) + 1] != '3' \
                        and title[i][len(re.match(Title[j].upper(), title[i]).group())] != '4' and title[i][
                    len(re.match(Title[j].upper(), title[i]).group()) + 1] != '5' and title[i][
                    len(re.match(Title[j].upper(), title[i]).group()) + 1] != '6':
                    Movie_Title[i] = Title[j]
                    Movie_Title_link[i] = Title_link[j]
                    Movie_certificate[i] = certificate[j]
                    Movie_lister_item_content[i] = lister_item_content[j]
                    Movie_ipl_rating_star_rating[i] = ipl_rating_star_rating[j]
                    Movie_runtime[i] = runtime[j]
                    Movie_lister_item_content1[i] = lister_item_content1[j]
                    Movie_genre[i] = genre[j]
                    Movie_inline_block[i] = inline_block[j]
                    Movie_Gross[i] = Gross[j]
                    Movie_Headline[i] = Headline[j]
                    Movie_Director[i] = Director[j]
                    Movie_Writers[i] = Writers[j]
                    Movie_Stars[i] = Stars[j]
                    Movie_Plot_Keywords[i] = Plot_Keywords[j]
                    Movie_Genres[i] = Genres[j]
                    Movie_Parents_Guide[i] = Parents_Guide[j]
                    Movie_Official_Sites[i] = Official_Sites[j]
                    Movie_Country[i] = Country[j]
                    Movie_Language[i] = Language[j]
                    Movie_Filming_Locations[i] = Filming_Locations[j]
                    Movie_Gross_USA[i] = Gross_USA[j]
                    Movie_Cumulative_Worldwide_Gross[i] = Cumulative_Worldwide_Gross[j]
                    Movie_Production_Co[i] = Production_Co[j]
                    Movie_Sound_Mix[i] = Sound_Mix[j]
                    Movie_Color[i] = Color[j]
                    Movie_Aspect_Ratio[i] = Aspect_Ratio[j]
                    Movie_Description[i] = Description[j]
                    Movie_Trailer[i] = Trailer[j]
                    Movie_UK_Release_Time[i] = UK_Release_Time[j]
                    Movie_Budget[i] = Budget[j]
                    Movie_US[i] = US[j]
                    Movie_Writers_2[i] = Writers_2[j]
                    Movie_Stars_2[i] = Stars_2[j]
                    Movie_Stars_3[i] = Stars_3[j]
                    Movie_Storyline[i] = Storyline[j]
                    Movie_Plot_Keywords_2[i] = Plot_Keywords_2[j]
                    Movie_Plot_Keywords_3[i] = Plot_Keywords_3[j]
                    Movie_Plot_Keywords_4[i] = Plot_Keywords_4[j]
                    Movie_Plot_Keywords_5[i] = Plot_Keywords_5[j]
                    # print('%s  %s  %s\n' % (Movie_Title[i], title[i], Movie_Title_link[i]))
    '''
                    print('%s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s  %s\n'%
                          (time[i], channelId[i], title[i], Trailer_series[i], description[i], categoryId[i], \
                           duration[i], viewCount[i], likeCount[i], dislikeCount[i], favoriteCount[i], commentCount[i], \
                           Stars[i], Directors[i], ReleaseTime[i], Synopsis[i], \
                           Movie_Title[i], Movie_Title_link[i], Movie_certificate[i], Movie_lister_item_content[i], \
                           Movie_ipl_rating_star_rating[i], Movie_runtime[i], Movie_lister_item_content1[i], Movie_genre[i], \
                           Movie_inline_block[i], Movie_Gross[i], Movie_Headline[i], Movie_Director[i], Movie_Writers[i], \
                           Movie_Stars[i], Movie_Plot_Keywords[i], Movie_Genres[i], Movie_Parents_Guide[i], \
                           Movie_Official_Sites[i], Movie_Country[i], Movie_Language[i], Movie_Filming_Locations[i], \
                           Movie_Gross_USA[i], Movie_Cumulative_Worldwide_Gross[i], Movie_Production_Co[i], Movie_Sound_Mix[i], \
                           Movie_Color[i], Movie_Aspect_Ratio[i], Movie_Description[i], Movie_Trailer[i], Movie_UK_Release_Time[i], \
                           Movie_Budget[i], Movie_US[i], Movie_Writers_2[i], Movie_Stars_2[i], Movie_Stars_3[i], Movie_Plot_Keywords_2[i], \
                           Movie_Plot_Keywords_3[i], Movie_Plot_Keywords_4[i], Movie_Plot_Keywords_5[i], Movie_Storyline[i]))
    '''
    for i in range(len(title)):
        print('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' \
              ',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' %
              (time[i], channelId[i], title[i], Trailer_series[i], description[i], categoryId[i], \
               duration[i], viewCount[i], likeCount[i], dislikeCount[i], favoriteCount[i], commentCount[i], \
               Stars[i], Directors[i], ReleaseTime[i], Synopsis[i], \
               Movie_Title[i], Movie_Title_link[i], Movie_certificate[i], Movie_lister_item_content[i], \
               Movie_ipl_rating_star_rating[i], Movie_runtime[i], Movie_lister_item_content1[i], Movie_genre[i], \
               Movie_inline_block[i], Movie_Gross[i], Movie_Headline[i], Movie_Director[i], Movie_Writers[i], \
               Movie_Stars[i], Movie_Plot_Keywords[i], Movie_Genres[i], Movie_Parents_Guide[i], \
               Movie_Official_Sites[i], Movie_Country[i], Movie_Language[i], Movie_Filming_Locations[i], \
               Movie_Gross_USA[i], Movie_Cumulative_Worldwide_Gross[i], Movie_Production_Co[i], Movie_Sound_Mix[i], \
               Movie_Color[i], Movie_Aspect_Ratio[i], Movie_Description[i], Movie_Trailer[i], Movie_UK_Release_Time[i], \
               Movie_Budget[i], Movie_US[i], Movie_Writers_2[i], Movie_Stars_2[i], Movie_Stars_3[i],
               Movie_Plot_Keywords_2[i], \
               Movie_Plot_Keywords_3[i], Movie_Plot_Keywords_4[i], Movie_Plot_Keywords_5[i], Movie_Storyline[i]))

        data = (time[i], channelId[i], title[i], Trailer_series[i], description[i], categoryId[i], \
                duration[i], viewCount[i], likeCount[i], dislikeCount[i], favoriteCount[i], commentCount[i], \
                Stars[i], Directors[i], ReleaseTime[i], Synopsis[i], \
                Movie_Title[i], Movie_Title_link[i], Movie_certificate[i], Movie_lister_item_content[i], \
                Movie_ipl_rating_star_rating[i], Movie_runtime[i], Movie_lister_item_content1[i], Movie_genre[i], \
                Movie_inline_block[i], Movie_Gross[i], Movie_Headline[i], Movie_Director[i], Movie_Writers[i], \
                Movie_Stars[i], Movie_Plot_Keywords[i], Movie_Genres[i], Movie_Parents_Guide[i], \
                Movie_Official_Sites[i], Movie_Country[i], Movie_Language[i], Movie_Filming_Locations[i], \
                Movie_Gross_USA[i], Movie_Cumulative_Worldwide_Gross[i], Movie_Production_Co[i], Movie_Sound_Mix[i], \
                Movie_Color[i], Movie_Aspect_Ratio[i], Movie_Description[i], Movie_Trailer[i], Movie_UK_Release_Time[i], \
                Movie_Budget[i], Movie_US[i], Movie_Writers_2[i], Movie_Stars_2[i], Movie_Stars_3[i],
                Movie_Plot_Keywords_2[i], \
                Movie_Plot_Keywords_3[i], Movie_Plot_Keywords_4[i], Movie_Plot_Keywords_5[i], Movie_Storyline[i])
        db.save_data(data)

