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
const checkboxs=document.querySelectorAll('.new-control-input')

// Set eventlistener
checkboxs.forEach(el=>el.addEventListener('click',()=>{togglecheck(event)}))
// Manage and switch between commands
class Selector {

    constructor() {
        runbtn.addEventListener('click', () => {
            this.swManage()
        })
        checkallbtn.addEventListener('click',()=>{
            if(checkallbtn.checked==true){
                ids=[]
                posts.querySelectorAll('tbody tr').forEach(el=>{
                        ids.push(el.getAttribute('data-field-number'))
                })
                console.log(ids)
                oncheck(ids)    
            }else{
                offcheck(ids)
                ids=[]
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

function togglecheck(e){
    let id=e.target.getAttribute('data-field-number')
    if(ids.includes(id)){
        removeItemOnce(ids,id)
    }else{
        ids.push(id)
     
    }
}

// delete item
class DeleteItem {
    //  properties
    status = false
    single=null
    backup=null
    ConfirmBtn = document.getElementById('btn_confirm_delete')
    AllElement = document.querySelectorAll("tr[data-field-number]")
    constructor() {
        this.AllElement.forEach((el) => {
            el.querySelector('.deleteBtn').addEventListener('click', () => {
                this.reset()
                this.getId(el.getAttribute('data-field-number'))
            })
        })
        this.ConfirmBtn.addEventListener('click', (e) => {
            if (!this.status) {
                this.ConfirmDeleted()
            }
        })
    }
    // methods
    getId(iid) {
        this.status = false
        this.backup = [Number(iid)]
    }

    mulitidelete(ids){
        this.backup=ids
    }
    ConfirmDeleted() {
        if (this.status == false) {
            this.status = true
            this.ConfirmBtn.querySelector('span').style.display = 'none'
            this.ConfirmBtn.querySelector('svg').style.display = "block";
            var self = this;
            axios({
                method: 'post',
                url: myurl,
                data: {
                    id: this.backup,
                },
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Accept: "application/json",
                }
            }).then(function (response) {
                    console.log(response)
                if (response.data['status']) {
                    self.Finnish(response.data['ids'])  
                }else{
                    throw new Error("Custom Error Message");
                }
            }).catch(function (error) {
                console.log(self.ConfirmBtn);
                self.ConfirmBtn.querySelector('span').innerHTML = "خطا در حذف، لطفا مجددا امتحان کنید."
                self.ConfirmBtn.querySelector('svg').style.display = 'none'
                self.ConfirmBtn.querySelector('span').style.display = 'block'

            }).finally(()=>{
            })
        }
    }
    reset(){
  
            this.ConfirmBtn.classList.remove('btn-success')
            this.ConfirmBtn.classList.add('btn-danger')
            this.ConfirmBtn.querySelector('span').innerHTML = "حذف"
            ids=[]
        
    }
    Finnish(items) {
        this.ConfirmBtn.querySelector('svg').style.display = "none";
        this.ConfirmBtn.classList.add('btn-success');
        this.ConfirmBtn.querySelector('span').style.display = 'block'
        this.ConfirmBtn.querySelector('span').innerHTML = "حذف شد!"
        document.querySelectorAll(`[data-field-number='${items}']`).forEach((el) => {
            el.remove()
        })
    }
}
const deleteItems = new DeleteItem();