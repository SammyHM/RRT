# Data Generation

<table>
  <tr>
    <td>
      <div style="font-weight: bold;">@property <br> JSON_PATH</div>
      <div style="font-style: italic;">Defines the file location where all json files are stored.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">@property <br> PDF_PATH</div>
      <div style="font-style: italic;">Defines the file location where all pdf files are stored.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def create_txt(content: str, article: str, lan: str = 'default') &rarr; str:</div>
      <div style="font-style: italic;">Creates a text file at 'out' directory with its corresponding content. Returns file path.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def save_pubs(pubs: list(), name: str) &rarr; None:</div>
      <div style="font-style: italic;">Given a list of Publication type objects, saves a json file representative of it.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def save_summaries(pubs: list(), name: str) &rarr; None:</div>
      <div style="font-style: italic;">Given a list of summaries, saves a json file representative of it.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def write_pdf_data(file_name: str, content: bytes) &rarr; None:</div>
      <div style="font-style: italic;">Given a file name, saves the content at pdf data path.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def parse_pdf_data(file_name:str) &rarr; str:</div>
      <div style="font-style: italic;">Given a file_name, parses its pdf data and returns its text formated.</div>
    </td>
  </tr>
</table>
