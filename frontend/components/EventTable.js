import React from "react";

const EventTable = ({ events }) => {
    return ( <
        div >
        <
        h2 > Historical Events Impacting Oil Prices < /h2> <
        table >
        <
        thead >
        <
        tr >
        <
        th > Date < /th> <
        th > Event < /th> <
        th > Impact < /th> <
        /tr> <
        /thead> <
        tbody > {
            events.map((event, index) => ( <
                tr key = { index } >
                <
                td > { event.date } < /td> <
                td > { event.event } < /td> <
                td > { event.impact } < /td> <
                /tr>
            ))
        } <
        /tbody> <
        /table> <
        /div>
    );
};

export default EventTable;