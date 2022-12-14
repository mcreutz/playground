async function getDataAsyncNotation() {
    const response = await fetch('http://myserver/endpoint', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });
    const data = await response.json();
    return data;
}


async function getDataThenNotation() {
    const response = fetch('http://localhost:5000/api/v1/entry')
        .then((res) => res.json())
        .then((res) => { console.log(res) });
    return data;
}