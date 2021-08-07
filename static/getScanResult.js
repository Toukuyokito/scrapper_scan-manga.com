function deleteChild(parent)
{
	while (parent.lastElementChild) {
		parent.removeChild(parent.lastElementChild);
	  }
}

function insertRow(parent, short, episode_number, older_episode_number, endpoint)
{
	const row = parent.insertRow();
	const cell = [];
	for(let i=0; i < 4; ++i)
	{
		cell.push(row.insertCell());

	}

	cell[0].innerHTML = short; 
	cell[1].innerHTML = episode_number; 
	cell[2].innerHTML = older_episode_number;
	cell[3].innerHTML = `<a target="__blank" href="${endpoint}">${endpoint}</a>`
	
}


function scan(e)
{
	
	fetch("/getData")
	.then(blob   => blob.json())
	.then(series => {
		
		const displayTarget = document.getElementById(e.target.dataset.target);
		deleteChild(displayTarget);

		for(serie of series.series)
		{
			insertRow(displayTarget,serie.short, 
					  serie.episode_number, 
					  serie.older_episode_number,
					  serie.url);
		}

	});

}

scanButton = document.querySelector(".scan-button");
scanButton.addEventListener("click", scan);