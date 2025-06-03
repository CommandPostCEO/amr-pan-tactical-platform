import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { FileUploader } from "@/components/ui/file-uploader";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Table, TableHead, TableRow, TableHeader, TableCell, TableBody } from "@/components/ui/table";

export default function CommandPostPro() {
  const [file, setFile] = useState(null);
  const [activeTab, setActiveTab] = useState("status");
  const [auditResults, setAuditResults] = useState([]);

  return (
    <div className="bg-black text-chalk min-h-screen font-mono">
      <div className="grid grid-cols-12 gap-2 p-4">
        {/* Sidebar Nav */}
        <aside className="col-span-2 bg-gray-900 p-4 rounded-2xl shadow-lg">
          <h2 className="text-xl font-bold mb-4">🛰️ Command Nav</h2>
          <TabsList className="flex flex-col gap-2">
            <TabsTrigger value="status" onClick={() => setActiveTab("status")}>🟢 Status</TabsTrigger>
            <TabsTrigger value="uploads" onClick={() => setActiveTab("uploads")}>📂 Uploads</TabsTrigger>
            <TabsTrigger value="reports" onClick={() => setActiveTab("reports")}>📊 Reports</TabsTrigger>
            <TabsTrigger value="threats" onClick={() => setActiveTab("threats")}>⚠️ Threats</TabsTrigger>
          </TabsList>
        </aside>

        {/* Main Dashboard */}
        <main className="col-span-10 space-y-4">
          <Card className="bg-gray-800 border border-olive">
            <CardContent className="p-4">
              <h1 className="text-3xl font-bold text-coyote">AMR Tactical PAN Audit</h1>
              <p className="text-chalk mt-1">Mission Control Panel – Last scan: N/A</p>
            </CardContent>
          </Card>

          {/* Tactical Alert Strip */}
          <div className="grid grid-cols-3 gap-2">
            <div className="bg-green-600 p-2 rounded text-center">✔️ Systems Nominal</div>
            <div className="bg-yellow-600 p-2 rounded text-center">⚠️ Manual Checks Pending</div>
            <div className="bg-red-700 p-2 rounded text-center">❗ Threats Detected</div>
          </div>

          {/* Upload UI */}
          {activeTab === "uploads" && (
            <Card className="bg-gray-700">
              <CardContent className="p-4">
                <h2 className="text-xl font-bold text-chalk">📂 Upload Excel File</h2>
                <FileUploader file={file} setFile={setFile} />
                <Button className="mt-4 bg-coyote text-black hover:bg-olive">Execute Scan</Button>
              </CardContent>
            </Card>
          )}

          {/* Reports Table */}
          {activeTab === "reports" && (
            <Card className="bg-gray-700">
              <CardContent className="p-4 overflow-auto">
                <h2 className="text-xl font-bold text-chalk mb-2">📊 Audit Log</h2>
                <Table className="text-xs whitespace-nowrap">
                  <TableHeader className="bg-olive text-black">
                    <TableRow>
                      <TableHead>PAN</TableHead>
                      <TableHead>Carrier</TableHead>
                      <TableHead>Status</TableHead>
                      <TableHead>Validation</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {auditResults.map((item, idx) => (
                      <TableRow key={idx} className={idx % 2 === 0 ? "bg-gray-800" : "bg-gray-700"}>
                        <TableCell>{item.pan}</TableCell>
                        <TableCell>{item.carrier}</TableCell>
                        <TableCell>{item.status}</TableCell>
                        <TableCell>{item.validation}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </CardContent>
            </Card>
          )}
        </main>
      </div>
    </div>
  );
}
