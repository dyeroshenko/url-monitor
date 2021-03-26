document.addEventListener("DOMContentLoaded", function () {

	const content = document.getElementById('content')
	const form = document.getElementById('form')
	const input = document.getElementById('url')
	const stats = document.getElementById('stats')

	form.addEventListener('submit', function (event) {
		const formData = new FormData(this);

		content.innerHTML = '';
		stats.innerHTML = '';

		fetch(`${window.origin}/post`, {
				body: formData,
				method: 'POST'
			})
			.then(function (response) {
				response.json()
					.then(function (data) {
						content.style.visibility = 'visible'
						if (data['message']) {
							content.innerHTML += `<span id='message-title'>${data['message']}<span>`
							if (data['code'] != 200) {
								content.style.backgroundColor = '#d14848'
							} else {
								content.style.backgroundColor = '#618a32'
								stats.style.visibility = 'visible'
								stats.innerHTML = `
								<ul>
									<li><span class='details-key'>HTTP Response:</span> <span class='details-value'>${data['code']}</span></li>
									<li><span class='details-key'>Host name:</span> <span class='details-value'>${data['host']}</span></li>
									<li><span class='details-key'>IP Address:</span> <span class='details-value'>${data['ip']}</span></li>
									<li><span class='details-key'>Round Trip Time:</span> <span class='details-value'>${data['round-trip-time']}</span></li>
								</ul>
								`
							}
						} else {
							content.innerHTML += `<span id='message-title'>Invalid URL! Try again</span>`
							content.style.backgroundColor = '#d14848'
						}
					});
			});
		event.preventDefault();
	});


	input.addEventListener('click', function (event) {
		event.preventDefault();

		content.style.visibility = 'hidden'
		stats.style.visibility = 'hidden'
	})

});