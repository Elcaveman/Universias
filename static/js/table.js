// let's use jquery for now
let array = []
var barray=[]
// let's get the url from the table
const table = document.getElementById('PostsTable')
const APIurl= table.attributes['api'].value
const user = table.attributes['user'].value

$.ajax({
    method:'GET',
    url:APIurl,
    success:(response)=>{
        array = response;
        populate_table(array)
    }
});
function populate_table(array){
    const table = document.getElementById("PostsTable")
    //let's clean the table first!
    table.innerHTML = '';
    function delete_btn_html(user1 , user2 ,row_data_id){
        if (user1==user2){
            return `<a href="/delete_post/${row_data_id}">
            <button class="btn btn-danger hidden">Delete</button></a>`
        }
        return ''

    }
    for (let i =0 ; i<array.length ; i++){
        row_data = array[i];
        rowHTML=`<tr>
        <td>${row_data.title}</td>
        <td>${row_data.pub_type}</td>
        <td>${row_data.owner}</td>
        <td>${row_data.timestamp}</td>
        <td>
            <a href="/posts/${row_data.id}">
                <button class="btn btn-info m-1">Info</button>
            </a>`+delete_btn_html(user , row_data.owner , row_data.id)
        +"</td></tr>";
        table.innerHTML += rowHTML;
    }
    barray = array;
};

function search(sub_string , text){
    let text_ = text.toLowerCase();
    //substring always is already lowercase
    const len = sub_string.length;
    for (let i =0 ; i<text.length-len ; i++){
        if(sub_string == text_.substring(i,i+len)){
            return true;
        }
    }
    return false;
}

function create_filtered_array(array , field , filter_word){
    let new_array = [];
    for (let i =0 ; i<array.length ; i++){
        row_data = array[i];
        boo= search(filter_word , row_data[field]);
        if (boo){new_array.push(row_data);}
    }
    return new_array
}
// search via searchbar
//TODO: filter by options so i can use the field arg to it's fullest!
const searchbar = document.querySelector("#search_input");

searchbar.addEventListener("keyup",(event)=>{
    let filter_word = searchbar.value.toLowerCase();
    //add filter by drop menu to chose 
    let new_array = create_filtered_array(array , 'title' , filter_word);
    populate_table(new_array);
    
}
)

// search via clicks
const title_filter = document.querySelector("[data-column='title']");
const type_filter = document.querySelector("[data-column='type']");
//const authors_filter = document.querySelector("[data-column='authors']");
const time_filter = document.querySelector("[data-column='timestamp']");

title_filter.addEventListener('click',()=>{
    barray.sort(compare_title);
    populate_table(barray);
})
type_filter.addEventListener('click',()=>{
    barray.sort(compare_type);
    populate_table(barray);
})
time_filter.addEventListener('click',()=>{
    barray.sort(compare_time);
    populate_table(barray);
})

// define all these niggers in a class with a juicy proto
function compare_date(a, b){
    // converts the timestamps of a and b to dates
    a = Date(a.timestamp)
    b = Date(a.timestamp)
    // a should come before b in the sorted order
    if(a < b){
            return -1;
    // a should come after b in the sorted order
    }else if(a > b){
            return 1;
    // a and b are the same
    }else{
            return 0;
    }
}
function compare_title(a,b){
     // converts the timestamps of a and b to dates
     a = a.title
     b = a.title
     // a should come before b in the sorted order
     if(a < b){
             return -1;
     // a should come after b in the sorted order
     }else if(a > b){
             return 1;
     // a and b are the same
     }else{
             return 0;
     }
}
function compare_type(a,b){
    // converts the timestamps of a and b to dates
    a = a.pub_type
    b = a.pub_type
    // a should come before b in the sorted order
    if(a < b){
            return -1;
    // a should come after b in the sorted order
    }
    else if(a > b){
            return 1;
    // a and b are the same
    }
    else{
            return 0;
    }}