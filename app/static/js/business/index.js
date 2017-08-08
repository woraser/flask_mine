/**
 * Created by chenhui on 2017/8/8.
 */
var indexController = {
    topicTable :null,
    init:function () {
        indexController.tableInit();
    },
    tableInit:function () {
        indexController.topicTable = $('#topicTable').dataTable({
			serverSide:true,
            processing: true,
            searching:false,
            paging: true,
			ordering:false,
			pageLength:10,
            bLengthChange:false,
            showNEntries: true,
            scrollCollapse: true,
            bInfo : true,
            destroy:true,
			language: {
			  emptyTable: "暂无数据",
              oPaginate : {
                    "sFirst" : "首页",
                    "sPrevious" : "上一页",
                    "sNext" : "下一页",
                    "sLast" : "末页"
                }
			},
            ajax: {
                url:"/common/dataTable/Topic",
                type:"POST",
                contentType : "application/json",
                data: function ( d ) {
                var draw = d['draw'];
                var post_data = {
                    offset :  d['start'],
                    pageSize :  d["length"],
                    pageNumber :  (d["start"] / d["length"] + 1),
                    draw :  d['draw'],
                    condition:null
                };
                //添加额外的参数传给服务器
                return JSON.stringify(post_data);
                }
            },
            columns: [
                { "title":"id","data": "id","orderable":false,"width":"15%"},
                { "title":"内容","data": "title","orderable":false,"width":"50%" }
                 ],
            columnDefs:[{
                targets: 2,
                render: function (data, type, row, meta) {
                    return '<a type="button" class="marked" href="#" onclick=indexController.markedSign("' + row.id + '") >标记</a>';
                }
            },
                { "orderable": false, "targets": 2 }
            ],
            fnCreatedRow:function(nRow, aData, iDataIndex){
			    //颜色擢用
			    if(aData["user"] == "chenhui"){
			        $(nRow).css("color","blue");
			        $(nRow).find(".marked").hide();
                }else if(aData["user"] == "zhaoshuang"){
			       $(nRow).css("color","pink");
			       $(nRow).find(".marked").hide();
                }
            }
        });
    },
    markedSign:function (id) {
        $.ajax({
			type:"GET",
			url:"/topicMark/"+id,
			success:function(result){
                var data = JSON.parse(result);
                 if(data["status"] != 1){
                     bootbox.alert("操作失败！");
                 }else {
                     indexController.topicTable.api().ajax.reload();
                 }
                }
            });
    },
    addTopic:function () {

    }
};


$(document).ready(function() {
	indexController.init();

// $("#back").click(function(){
// $.openDialog({width:"700",height:"500",jq:$("#secondLevelDialog"),titleText:"配置",url:"html/iotxnew/edit.html"});
// });

});
