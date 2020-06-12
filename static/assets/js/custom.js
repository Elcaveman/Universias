//chart-posts , chart-users
//Charts
//line chart
//
var object;

$.ajax({
  //form of the api response:
  // {
  //   "posts_by_type_monthly": [["2020-06-01T00:00:00Z", "Document", 1]],
  //    "posts_by_domaine_total": [["AI", 1],["BI", 2]],
  //     "posts_by_revue_total": [["SCOPUS", 1]]
  //   }
  //limit array lenth to 10 set in the backend
  // use toLocaleString('default',{month:'short'}) to get month from date object
  method:'GET',
  url:'/charts/',
  success:(response)=>{
      object = response;
      console.log(object)
      makecharts(object)
  }
});
function extract(label_list,chart_data_list , shift){
  let dico = {}//label:data_list
  if (shift==0){
    dico = {
      labels : [],
      values: []
    }
    for (let i=0;i<chart_data_list.length;i++){
      dico.labels.push(chart_data_list[i][shift]) 
      dico.values.push(chart_data_list[i][shift+1]) 
    }
    return dico
  }
  else{
    // cahrt_data_list form : ["label",count](shift=0) if shift =1 : ['_','label',count]
    
    label_list.forEach((elt)=>{
      dico[elt]=[]
    })

    for (let i=0;i<chart_data_list.length;i++){
      dico[chart_data_list[i][shift]].push(chart_data_list[i][shift+1])
    }

    return dico
  }
  
  
}
function create_line_dataset(LABELLIST,COLORLIST,data_dico){
    let array = [];
    for (let i=0;i<LABELLIST.length;i++){
      if (data_dico[LABELLIST[i]]){
        array.push({
          data:data_dico[LABELLIST[i]],
          label:LABELLIST[i],
          borderColor:COLORLIST[i],
          fill:false
        })
      }
    }
    return array;  
  }
function makecharts(object) {
  var LABELLIST = ['Document','Project','conference paper','Brevet','Prototype']
  var COLORLIST = ['#3e95cd','#8e5ea2','#3cba9f','#e8c3b9','#c45850']
  let data_dico_posts_by_type_monthly = extract(LABELLIST , object.posts_by_type_monthly , 1)
  let data_dico_posts_by_domaine_total = extract([], object.posts_by_domaine_total , 0)
  let data_dico_posts_by_revue_total = extract([] , object.posts_by_revue_total , 0)

  let setting = {
    type: 'line',
    data: {
      labels: [...new Set(Array(object.posts_by_type_monthly.length).fill().map((_ , counter)=>{
        let date = new Date(object.posts_by_type_monthly[counter][0])
        return date.toLocaleString('default',{month:'short'})
      }))]//to remove duplicates
      ,
      // datasets elements format:{ 
      //   data: [86,114,106,106,107,111,133,221,783,2478],
      //   label: "Africa",
      //   borderColor: "#3e95cd",#8e5ea2,#3cba9f,#e8c3b9,#c45850
      //   fill: false
      // }
      // need to refactor the method i used is so inefficiente
      datasets: create_line_dataset(LABELLIST,COLORLIST,data_dico_posts_by_type_monthly) ,
    },
    options: {
      title: {
        display: false,
      }
    }
  }
  ['Document','Project','conference paper','Brevet','Prototype']
  setting = {
    type: 'line',
    data: {
      labels: [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015],
      datasets: [{ 
          data: [8,14,16,16,17,11,33,21,73,28],
          label: "Document",
          borderColor: "#3e95cd",
          fill: false
        }, { 
          data: [28,35,41,50,35,80,47,12,10,67],
          label: "Project",
          borderColor: "#8e5ea2",
          fill: false
        }, { 
          data: [16,17,17,19,20,27,40,54,67,73],
          label: "Conference paper",
          borderColor: "#3cba9f",
          fill: false
        }, { 
          data: [40,20,10,16,24,38,74,17,50,78],
          label: "Prototype",
          borderColor: "#e8c3b9",
          fill: false
        }, { 
          data: [6,3,2,2,7,6,8,12,12,4],
          label: "Brevet",
          borderColor: "#c45850",
          fill: false
        }
      ]
    },
    options: {
      title: {
        display: false,
      }
    }
  };


  console.log(setting)
  let PostsChart = new Chart(document.getElementById("chart-posts"), setting);

// Bar chart
let UserChart = new Chart(document.getElementById("chart-users"), {
    type: 'bar',
    data: {
      labels: data_dico_posts_by_domaine_total.labels,
      datasets: [
        {
          label: "Post count",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: data_dico_posts_by_domaine_total.values
        }
      ]
    },
    options: {        
      legend: { display: false },
      title: {
        display: false
      },
      scales: {
        yAxes: [{
            display: true,
            ticks: {
                suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
                // OR //
                beginAtZero: true   // minimum value will be 0.
            }
        }]
    }
    }
});

let UserChartdummy = new Chart(document.getElementById("chart-users2"), {
    type: 'bar',
    data: {
      labels: data_dico_posts_by_revue_total.labels,
      datasets: [
        {
          label: "Post count",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: data_dico_posts_by_revue_total.values
        }
      ]
    },
    options: {        
      legend: { display: false },
      title: {
        display: false,
      },
      scales: {
        yAxes: [{
            display: true,
            ticks: {
                suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
                // OR //
                beginAtZero: true   // minimum value will be 0.
            }
        }]
    }
    }
});
}
