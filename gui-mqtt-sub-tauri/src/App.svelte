<script>
    import Greet from './lib/Greet.svelte'
    import axios from 'axios';
    let readApiKey = 'UZSQG60FK8RA0ANW';
    let channelID = '2088972';
    // let readDataUrl = `https://api.thingspeak.com/channels/${channelID}/feeds.json?api_key=${readApiKey}`;

    let readDataUrl = (readApiKey, channelID) => ( `https://api.thingspeak.com/channels/${channelID}/feeds.json?api_key=${readApiKey}`);

    const options = { dateStyle: 'medium', timeStyle: 'short'};

    let cleanDate = (date) => {
        
        const newDate = new Date(date);
        return (newDate.toLocaleString("en-IN", options));
    }

    let promise = axios.get(readDataUrl(readApiKey, channelID));
</script>

<main class="font-roboto-flex">
    <h1> Thingspeak MQTT Subscribe display </h1>
    <div class="actions">
        <div class="inputs">
            <span>API Key:</span> <input placeholder="Enter your read API key" bind:value={readApiKey}/>
            <span>Channel ID:</span> <input placeholder="Enter your Channel ID" bind:value={channelID}/>
        </div>
        <button on:click={() => (promise = axios.get(readDataUrl(readApiKey, channelID)))}>
            <span class="material-symbols-rounded"> refresh </span>
        </button>
    </div>
    <div class="card">
        <span> Entry </span>
        <span> Time </span>
        <span> Temp <span class="material-symbols-rounded"> device_thermostat </span> </span>
        <span> Hum <span class="material-symbols-rounded"> humidity_percentage </span> </span>
        {#await promise}
            loading...
        {:then json}
                {#each json.data.feeds as records}
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
                            {#if records.field1 == null}
                                <span style="opacity: 0.2">-</span>
                            {:else}
                                {records.field2} %
                            {/if}       
                        </span>
                {/each}
        {/await}
    </div>
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
