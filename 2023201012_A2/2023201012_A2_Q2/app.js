
const clientId="a21aaa47fa7c4c958179036cecf513df";
const clientSecret="466aa644c1cf44e2b4a3390bde428cec";

async function getToken() 
{
    const result=await fetch("https://accounts.spotify.com/api/token", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + btoa(clientId + ":" + clientSecret)
        },
        body: "grant_type=client_credentials"
    });
    const data = await result.json();
    return data.access_token;
}


async function searchArtist(artistName) 
{
    const accessToken=await getToken();
    const searchQuery=encodeURIComponent(artistName);
    const url=`https://api.spotify.com/v1/search?q=${searchQuery}&type=artist`;
    
    try {
        const response=await fetch(url, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        const data=await response.json();

        if (data.artists && data.artists.items.length > 0) {
            const artist=data.artists.items[0];
            return artist;
        } else {
            console.error('Artist not found.');
            return null;
        }
    } catch (error) {
        console.error('Error searching for artist:', error);
        throw error;
    }
}

function displayArtistDetails(artist) 
{
    if(artist)
    {
        // console.log(artist);
        const artistNameElement=document.getElementById('name');
          // console.log(artist.name);
        artistNameElement.innerHTML=artist.name;
        const artistImageElement=document.getElementById('artist-image');
          // console.log(artist.images);
        artistImageElement.src=artist.images[1]?.url;
        const artistFollowersElement=document.getElementById('artist-followers');
        // console.log(artist.followers.total);
        artistFollowersElement.textContent=`Followers: ${artist.followers.total}`;
        const artistGenresElement=document.getElementById('artist-genres');
        // console.log(artist.genres);
        artistGenresElement.textContent=`Genres: ${artist.genres.join(', ')}`;
        const artistPopularity=document.getElementById('artist-popularity');
        artistPopularity.textContent=`Popularity: ${artist.popularity}`;
        const artistDetails=document.querySelector('.artist-details');
        artistDetails.childNodes[1].style.visibility="hidden";
        artistDetails.style.visibility="visible";
    }
    else
    {
        const artistDetails=document.querySelector('.artist-details');
        artistDetails.childNodes[1].innerHTML="Artist Not found";
        artistDetails.childNodes[1].style.visibility="visible";
        artistDetails.style.visibility="hidden";
    }
}

async function getArtist() 
{
    const artistName=document.getElementById('artist-name').value;
    try {
        const artist=await searchArtist(artistName);
        displayArtistDetails(artist);
    } catch (error) {
        console.error('Error:', error);
    }
}
