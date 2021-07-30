function __deleteChild(parentId)
{
	let parent = document.getElementById(parentId);

	while (parent.lastElementChild) {
		parent.removeChild(parent.lastElementChild);
	  }
}

function __showDataInDom(parentId, 
						 short, 
						 episode_number, 
						 older_episode_number,
						 siteUrl)
{

	let parent = document.getElementById(parentId);

	line                 = document.createElement("tr");
	columnName           = document.createElement("td");
	columnCurrentEpisode = document.createElement("td");
	columnEpisodeBefore  = document.createElement("td");
	columnUrl  			 = document.createElement("td");
	url                  = document.createElement("a");

	columnName.textContent             = short;
	columnCurrentEpisode.textContent   = episode_number; 
	columnEpisodeBefore.textContent    = older_episode_number;
	
	columnUrl.append(url);
	url.setAttribute("href", siteUrl);
	url.setAttribute("target", "__blank");
	url.textContent = siteUrl;

	line.append(columnName);
	line.append(columnCurrentEpisode);
	line.append(columnEpisodeBefore);
	line.append(columnUrl);

	parent.append(line)
	
	
		
}

function getScanResult(target)
{
	let request = new XMLHttpRequest();
	
	request.open("GET", "/getData", true);
	request.setRequestHeader('Content-type', 'application/json');
	
	request.onreadystatechange = function() {
		
		if (request.readyState === XMLHttpRequest.DONE && 
		    request.status     ===  200) {
		
			let answer = JSON.parse(request.responseText);
			__deleteChild(target)
			
			if (!answer) return;

			for (let serie of answer.serie ) {

				__showDataInDom(target, 
					            serie.short, 
								serie.episode_number, 
								serie.older_episode_number,
								serie.url);
			}
		}
	};

	request.send();

}
