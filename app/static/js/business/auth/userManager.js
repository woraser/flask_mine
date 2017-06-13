/**
 * Created by chenhui on 2017/6/9.
 */
var userMangerController = {
    init:function(){
        userMangerController.initTable();
    },
    initTable:function(){
        $('#userDiv').dataTable({
            serverSide:true,
            processing: true,
            searching:false,
            paging: true,
            bLengthChange:false,
            pageLength:1,
            ordering:false,
            // aLengthMenu:[1,2],
            showNEntries: false,
            scrollCollapse: true,
            bInfo : true,
            destroy:true,
            ajax: {
                url:"/common/dataTable/User",
                type:"POST",
                contentType : "application/json",
                data: function ( d ) {
                var draw = d['draw'];
                var post_data = {
                    offset :  d['start'],
                    pageSize :  d["length"],
                    pageNumber :  (d["start"] / d["length"] + 1),
                    draw :  d['draw']
                };
                //添加额外的参数传给服务器
                return JSON.stringify(post_data);
                }
            },
            columns: [
                { "title":"id","data": "id","orderable":false },
                { "title":"用户账号","data": "account","orderable":false },
                { "title":"创建时间","data": "created_time","orderable":false }
            ],
             columnDefs:[{
                targets: 2,
                render: function (data, type, row, meta) {
                    return '<a type="button" class="" href="#" onclick=showDetail(' + row.id + ') >查看详情</a>' +' | '+
                        '<a type="button" class="" href="#" onclick=updateSetting(' + row.id + ') >修改</a>';
                }
            },
                { "orderable": false, "targets": 2 }
            ]
        });
    }


};


$(document).ready(function() {
   userMangerController.init()

});