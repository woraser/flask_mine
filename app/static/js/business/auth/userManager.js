/**
 * Created by chenhui on 2017/6/9.
 */
var userMangerController = {
    init:function(){
        userMangerController.initTable();
    },
    initTable:function(){
        $('#userDiv').dataTable({
            processing: true,
            searching:false,
            paging: false,
            bLengthChange:false,
            showNEntries: false,
            scrollCollapse: true,
            bInfo : false,
            destroy:true,
            ajax: "/auth/userTable",
            columns: [
                { "title":"id","data": "id","orderable":false },
                { "title":"用户账号","data": "account","orderable":false },
                { "title":"创建时间","data": "created_time","orderable":false }
            ],
             columnDefs:[{
                targets: 3,
                render: function (data, type, row, meta) {
                    // return '<a type="button" class="" href="#" onclick=showDetail(' + row.id + ') >查看详情</a>' +' | '+
                    //     '<a type="button" class="" href="#" onclick=updateSetting(' + row.id + ') >修改</a>';
                }
            },
                { "orderable": false, "targets": 4 },
            ]
        });
    }


};


$(document).ready(function() {
   userMangerController.init()

});