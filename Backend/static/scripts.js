const current_song = document.querySelector('.current-song')
const btn_play = document.querySelector('.btn-play')
const btn_pause = document.querySelector('.btn-pause')
const btn_back = document.querySelector('.btn-back')
const btn_next = document.querySelector('.btn-next')
const btn_home = document.querySelector('.btn-home')
const progress = document.querySelector('.progress-bar')
const play_bar = document.querySelector('.play-bar')

var playButtons = document.getElementsByClassName('btn-float');
var artistFilters = document.getElementsByClassName('artist-filter');

window.onSpotifyWebPlaybackSDKReady = async () => {
    disabledAll()
    let interval;
    const accessToken = await getSessionData();
    const player = new Spotify.Player({
        name: 'Your Player Name',
        getOAuthToken: function(callback) {
            // Provide your Spotify access token here
            var _accessToken = accessToken
            console.log(_accessToken)
            callback(_accessToken);
        }
    });
    
    // Connect to the Spotify player
    player.connect().then(success => {
        if(success)
            console.log('Connected to Spotify player');
    }).catch((error) => {
        console.log(error)
    });
    
    // Function to play a song
    function playSong(trackUri) {
            // Play the song
        player._options.getOAuthToken(function(token) {
            fetch('https://api.spotify.com/v1/me/player/play', {
                method: 'PUT',
                headers: {
                    'Authorization': 'Bearer ' + token,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    uris: [trackUri]
                })
            });
        });
    }
    // Function to pause the currently playing song
    function pauseSong() {
        player._options.getOAuthToken(function(token) {
            fetch('https://api.spotify.com/v1/me/player/pause', {
                method: 'PUT',
                headers: {
                    'Authorization': 'Bearer ' + token,
                    'Content-Type': 'application/json'
                }
            });
        });
        pauseInterval()
    }
    
    // Function to resume the paused song
    function resumeSong() {
        player._options.getOAuthToken(function(token) {
            fetch('https://api.spotify.com/v1/me/player/play', {
                method: 'PUT',
                headers: {
                    'Authorization': 'Bearer ' + token,
                    'Content-Type': 'application/json'
                },
                body: ""
            });
        });
        startInterval()
    }

    function seekSong(position) {
        player._options.getOAuthToken(function(token) {
            fetch('https://api.spotify.com/v1/me/player/seek?' + new URLSearchParams({position_ms: position}), {
                method: 'PUT',
                headers: {
                    'Authorization': 'Bearer ' + token,
                    'Content-Type': 'application/json'
                }
                // body: ""
            });
        });
    }

    function getCurrentPlaying(){
        player._options.getOAuthToken(async function(token) {
            response = await fetch('https://api.spotify.com/v1/me/player/currently-playing', {
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer ' + token,
                    'Content-Type': 'application/json'
                }
                // body: ""
            });
            data = await response.json();
            console.log(data)
            progress.max = data['item']['duration_ms'] / 1000;
            progress.value = 0
            console.log(progress.max)
            // for(var i = 0; i < interval; i++)
            //     clearInterval(i)
            startInterval()
        });
    }
    
    function updateValue() {
        progress.value++;
        if(progress.value == progress.max){
            progress.value = 0;
            btn_play.display = ''
            btn_pause.display = 'none'
            disabledAll();
            clearInterval(interval);
        }
      }

    function startInterval() {
        // Start updating the value every second
        // clearInterval(interval)
        interval = setInterval(updateValue, 1000);
    }

    function pauseInterval() {
        // Pause the interval
        clearInterval(interval);
    }

    
      
   
    for (var i = 0; i < playButtons.length; i++) {
        playButtons[i].addEventListener('click', async function() {
            enabledAll()
            current_song.style.display = ''
            play_bar.style.height = ''
            play_bar.style.width = '';
            var songUrl = this.dataset.song_url; // Get the song ID from the data attribute

            const currentImg = document.querySelector('.current-img')
            currentImg.src = this.dataset.song_thumb; // Get the song ID from the data attribute
            const currentName = document.querySelector('.current-name')
            currentName.innerHTML = this.dataset.song_artist; // Get the song ID from the data attribute
            const currentArtist = document.querySelector('.current-artist')
            currentArtist.innerHTML = this.dataset.song_name; // Get the song ID from the data attribute
            btn_play.style.display='none'
            btn_pause.style.display=''
            progress.value = 0
            
            if (songUrl) {
                
                playSong(songUrl)
                getCurrentPlaying()
    
                // Play button clicked
                btn_play.addEventListener('click', function() {
                    btn_pause.style.display=''
                    btn_play.style.display='none'
                    resumeSong()
                });
                    
                // Pause button clicked
                btn_pause.addEventListener('click', function() {
                    btn_play.style.display=''
                    btn_pause.style.display='none'
                    pauseSong()
                });
                    
                // Progress bar dragged
                progress.addEventListener('input', (event) => {
                    const value = event.target.value;
                    seekSong(parseInt(value * 1000))
                    console.log('Value changed:', value);
                    // Perform any desired actions with the new value
                  });

                // player.load()
                // Update progress bar as the song plays     
                // const interval = setInterval(updateValue, 1000);        
                
            }
        });
    }

    for (var i = 0; i < artistFilters.length; i++){
        artistFilters[i].addEventListener('click', function(){
            updateFilteredData(this.dataset.artist_name);
        })
    }

    btn_home.addEventListener('click', function(){
        const mainItems = document.querySelectorAll('.main-item');
    
        for(var i = 0; i < mainItems.length; i++)
            mainItems[i].style.display = ''
    })
}

async function getSessionData() {
    try {
        const response = await fetch('/get-session-data');
        const data = await response.json();
        console.log(data['access token'])
        return data['access token'];
    } catch (error) {
        console.error('Error fetching session data:', error);
        return null;
    }
}

function disabledAll(){
    btn_back.disabled = true;
    btn_next.disabled = true;
    btn_play.disabled = true;
    // btn_pause.disabled = true;
    progress.disabled = true;
}

function enabledAll(){
    btn_back.disabled = false;
    btn_next.disabled = false;
    btn_play.disabled = false;
    // btn_pause.disabled = true;
    progress.disabled = false;
}

function updateFilteredData(artist_name) {
    const mainItems = document.querySelectorAll('.main-item');
    
    for(var i = 0; i < mainItems.length; i++)
        if(mainItems[i].dataset.artist_name != artist_name)
            mainItems[i].style.display = 'none'
        else
            mainItems[i].style.display = ''
}
