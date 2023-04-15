<script>
    import axios from 'axios';
    import {connect} from 'mqtt/dist/mqtt.min';

    import { subdata } from './lib/subdata.js';
    let readApiKey = 'UZSQG60FK8RA0ANW';
    let channelID = '2088972';

    let toEpoch = (timestamp) => {
        let date = new Date(timestamp);
        return date.getTime();
    }

    let readDataUrl = (readApiKey, channelID) => ( `https://api.thingspeak.com/channels/${channelID}/feeds.json?api_key=${readApiKey}`);

    const options = { dateStyle: 'medium', timeStyle: 'short'};

    const url = 'ws://mqtt3.thingspeak.com:80/mqtt'

    const mqtt_options = {
        clean: true,
        connectTimeout: 4000,
        username:'IjUVEwcKGjglLBIEMg0KABU',
        clientId:'IjUVEwcKGjglLBIEMg0KABU',
        password:'gygPM9XqkckFb9BWgJPy2SAg',
    }
    const client  = connect(url, mqtt_options)
    client.on('connect', () => {
        console.log('connected')
        client.subscribe(`channels/${channelID}/subscribe`, () => {
            console.log('subscribed to channel');
        })
    })

    client.on('message', function (topic, message) {
        // extradata.push(JSON.parse(message.toString()))
        subdata.update(records => ([JSON.parse(message.toString()), ...records]))
        // console.log(extradata)
    })

    let cleanDate = (date) => {
        
        const newDate = new Date(date);
        return (newDate.toLocaleString("en-IN", options));
    }

    let promise = axios.get(readDataUrl(readApiKey, channelID));
        /* <button on:click={() => (promise = axios.get(readDataUrl(readApiKey, channelID)))}>
            <span class="material-symbols-rounded"> refresh </span>
        </button> */
</script>

<main class="font-roboto-flex">
    <h1> Thingspeak MQTT Subscribe display </h1>
    <div class="actions">
        <div class="inputs">
            <span>API Key:</span> <input placeholder="Enter your read API key" bind:value={readApiKey}/>
            <span>Channel ID:</span> <input placeholder="Enter your Channel ID" bind:value={channelID}/>
        </div>
    </div>
    <div class="card">
        <span> Entry </span>
        <span> Time </span>
        <span> Temp <span class="material-symbols-rounded"> device_thermostat </span> </span>
        <span> Hum <span class="material-symbols-rounded"> humidity_percentage </span> </span>
    </div>
        {#each $subdata as records}
            <div class="card">
                    <span> {records.entry_id}  </span> 
                    <span> {cleanDate(records.created_at)} </span>
                    <span> 
                        {#if records.field1 == null}
                            <span style="opacity: 0.2">-</span>
                        {:else}
                            {records.field1} &#8451;
                        {/if}       
                    </span>
                    <span> 
                        {#if records.field2 == null}
                            <span style="opacity: 0.2">-</span>
                        {:else}
                            {records.field2} %
                        {/if}       
                    </span>
                </div>
            {/each}
        {#await promise}
            loading...
        {:then json}
                {#each json.data.feeds.reverse() as records}
                <div class="card">
                        <span> {records.entry_id}  </span> 
                        <span> {cleanDate(records.created_at)} </span>
                        <span> 
                            {#if records.field1 == null}
                                <span style="opacity: 0.2">-</span>
                            {:else}
                                {records.field1} &#8451;
                            {/if}       
                        </span>
                        <span> 
                            {#if records.field2 == null}
                                <span style="opacity: 0.2">-</span>
                            {:else}
                                {records.field2} %
                            {/if}       
                        </span>
                    </div>
                {/each}
        {/await}
</main>

<style>

.actions > button {
    width: fit-content;
    background: #ffffff22;
    padding: 0.4rem;
    border: 1px solid #ffffff33;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: 0.1s ease-in-out;
    color: white;
}

.actions > button:hover {
    border: 1px solid #ffffff55;
    background-color: #ffffff33;
}

.actions > button:active {
    border: 1px solid #ffffff66;
    background-color: #ffffff55;
}

main {
    display: flex;
    flex-direction: column;
    font-size: 1.3rem;
}

h1 {
    padding: 0rem 2rem;
    font-size: 3.3rem !important;
    font-weight: 500 !important;
}

.card {
    display: grid;
    grid-template-columns: 1fr 4fr 2fr 2fr; 
    max-width: 1080px;
    gap: 1.8rem 4rem;
    padding: 0.8rem 2rem;
}

.card > span {
    display: flex;
    align-items: center;
}

.actions {
    margin: 1rem 2rem;
    display: flex;
    align-items: center;
    justify-content: between;
}

.actions > .inputs {
    flex: 1;
    display: flex;
    align-items: center;
    gap: 0rem 1rem;
}

.inputs > input {
    background: #ffffff11;
    padding: 0.8rem 1.5rem;
    border-radius: .6rem;
    border: none;
    color: white;
    font-family: inherit;
    border: 1px solid #ffffff33;
}

</style>
