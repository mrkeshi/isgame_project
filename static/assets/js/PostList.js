//  delete once item in array

function removeItemOnce(arr, value) {
    var index = arr.indexOf(value);
    if (index > -1) {
        arr.splice(index, 1);
    }
    return arr;
}

// id
let id = 0
let ids = []

// buttons & elements
const checkallbtn = document.getElementById('All_Checked')
const runbtn = document.getElementById('runBtn')
const filterbtn = document.getElementById('filter')
const selectorinput = document.getElementById('selectRun')
const posts=document.getElementById('result_list_post')

// Manage and switch between commands
class Selector {

    constructor() {
        runbtn.addEventListener('click', () => {
            this.swManage()
        })

        checkallbtn.addEventListener('click',()=>{
            if(checkallbtn.checked){
                posts.querySelectorAll('tbody tr').forEach(el=>{
                    if(el.getAttribute('data-field-number') in ids){alert('hast')}
                    ids.push(el.getAttribute('data-field-number'))
                })
                console.log(ids)
                oncheck(ids)    
            }else{
                posts.querySelectorAll('tbody tr').forEach(el=>{
                    removeItemOnce(ids,(el.getAttribute('data-field-number')))
        
                })
                offcheck(ids)
            }
        })
    }
    swManage() {
        alert(posts.querySelectorAll('tbody tr').length)
        switch (selectorinput.value) {
            case 'delete':
                deleteItem()
                break;

            case 'draft':
                draftOrpost("draft")
                break;

            case 'post':
                draftOrpost("post")
                break;
            default:
                break;
        }
    }
}
new Selector()

// function for send request and doing commands
const deleteItem = () => {
    return 0;
}
const draftOrpost = (key) => {
    return 0;
}

// check
function oncheck(ids){
    ids.forEach(id => {
        posts.querySelector(`tbody tr[data-field-number='${id}'] .new-control-input`).checked=true
    });
  
}
// off check
function offcheck(ids){
    ids.forEach(id => {
        posts.querySelector(`tbody tr[data-field-number='${id}'] .new-control-input`).checked=false
    });
  
}