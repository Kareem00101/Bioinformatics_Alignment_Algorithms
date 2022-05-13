var row=0
var col=0
var cell="#c" + row + col

document.querySelector('#show').addEventListener('click',()=>{
    console.log("here1", cell)
    
    document.querySelector(cell).style.visibility="hidden";
    col ++;
    cell="#c" + row + col;
    console.log(cell)
});

 document.querySelector("#traceBack").addEventListener('click',()=>{

    if(document.getElementById("withTrace").style.display=="flex"){
        document.getElementById("withoutTrace").style.display="flex";
        document.getElementById("withTrace").style.display="none";
    }else{
        document.getElementById("withoutTrace").style.display="none";
        document.getElementById("withTrace").style.display="flex";
    }
}) 



// <div id="alignment">
//                 <div class="row">
//                     {%for i in range(alignment|length/2%}
//                         <div class="col">
//                             {%for a in alignment%}
//                                 <p>{{}}</p>
//                             {%endfor%}
//                         </div>
//                     {%endfor%}
//                 </div>
//             </div>


{/* <div id="withoutTrace">
                        <tr>
                            <th class="cellh">0</th>
                            {%for i in range((s1|length +1))%}
                                <td> 
                                    <span id=c{{0}}{{i}} class="cell">{{l1[0][i]}} </span> 
                                </td>
                            {%endfor%}
                        </tr>
                    </div>

                    <div id="withTrace">
                        <tr>
                            <th class="cellh">0</th>
                            {%for i in range((s1|length +1))%}
                                    {%if i1[0][i] == 1 %}
                                        <td>
                                            <span id=c{{0}}{{i}} class="cellC">{{l1[0][i]}} </span>
                                        </td>
                                    {%else%}
                                        <td>
                                            <span id=c{{0}}{{i}} class="">{{l1[0][i]}}</span>
                                        </td>
                                    {%endif%}
                            {%endfor%}
                        </tr>
                    </div>
                    {%for d in range((s2|length)) %}

                        <div id="withoutTrace">
                            <tr>
                                <th scope="row" class="cellh">{{s2[d]}}</th>
                                {%for i in range((s1|length +1))%}
                                        <td>
                                            <span id=c{{d+1}}{{i}} class="cell">{{l1[d+1][i]}} </span>
                                        </td>
                                {%endfor%}
                            </tr>
                        </div>

                        <div id="withTrace">
                            <tr>
                                <th scope="row" class="cellh">{{s2[d]}}</th>
                                {%for i in range((s1|length +1))%}
                                    {%if i1[d+1][i] == 1 %}
                                        <td>
                                            <span id=c{{d+1}}{{i}} class="cellC">{{l1[d+1][i]}} </span>
                                        </td>
                                    {%else%}
                                        <td>
                                            <span id=c{{d+1}}{{i}} class="">{{l1[d+1][i]}} </span>
                                        </td>
                                    {%endif%}
                                {%endfor%}
                            </tr>
                        </div>

                    {%endfor%} */}